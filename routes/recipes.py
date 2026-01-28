"""
Recipe routes for browsing, searching, and viewing recipes
"""
from flask import Blueprint, render_template, jsonify, request
from models.recipe import Recipe

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/')
def browse():
    """Browse all recipes with optional filtering"""
    # Get filter parameters
    category = request.args.get('category', None)
    tag = request.args.get('tag', None)
    page = request.args.get('page', 1, type=int)
    per_page = 12
    
    # Build query
    query = Recipe.query
    
    if category:
        query = query.filter_by(category=category)
    
    if tag:
        query = query.filter(Recipe.tags_json.contains(tag))
    
    # Paginate results
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    recipes = pagination.items
    
    # Get all unique categories and tags for filters
    all_categories = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
    all_tags = ['Vegetarian', 'Vegan', 'Gluten-Free', 'Diabetes-Friendly', 'High-Protein', 'Low-Carb']
    
    return render_template('recipes/browse.html', 
                         recipes=recipes,
                         pagination=pagination,
                         categories=all_categories,
                         tags=all_tags,
                         current_category=category,
                         current_tag=tag)

@recipes_bp.route('/<int:recipe_id>')
def detail(recipe_id):
    """View recipe detail"""
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipes/detail.html', recipe=recipe)

@recipes_bp.route('/api/search')
def search():
    """Search recipes by name or description (JSON API)"""
    query_string = request.args.get('q', '')
    
    if not query_string:
        return jsonify({'recipes': []})
    
    # Search in name and description
    recipes = Recipe.query.filter(
        (Recipe.name.ilike(f'%{query_string}%')) | 
        (Recipe.description.ilike(f'%{query_string}%'))
    ).limit(20).all()
    
    return jsonify({
        'recipes': [recipe.to_dict() for recipe in recipes]
    })

@recipes_bp.route('/api/filter')
def filter_recipes():
    """Filter recipes by category and tags (JSON API)"""
    category = request.args.get('category')
    tags = request.args.getlist('tags')
    
    query = Recipe.query
    
    if category:
        query = query.filter_by(category=category)
    
    for tag in tags:
        query = query.filter(Recipe.tags_json.contains(tag))
    
    recipes = query.all()
    
    return jsonify({
        'recipes': [recipe.to_dict() for recipe in recipes]
    })
