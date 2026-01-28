"""
Main routes for homepage and general pages
"""
from flask import Blueprint, render_template
from models.recipe import Recipe

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Homepage with hero section and featured recipes"""
    # Get 6 featured recipes for homepage
    featured_recipes = Recipe.query.limit(6).all()
    return render_template('index.html', featured_recipes=featured_recipes)

@main_bp.route('/about')
def about():
    """About page"""
    return render_template('about.html')
