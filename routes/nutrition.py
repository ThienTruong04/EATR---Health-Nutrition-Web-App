"""
Nutrition tracking routes
"""
from flask import Blueprint, render_template, jsonify, request
from models import db
from models.user import User
from models.meal_plan import MealPlan
from models.recipe import Recipe
from datetime import datetime, timedelta

nutrition_bp = Blueprint('nutrition', __name__, url_prefix='/nutrition')

@nutrition_bp.route('/dashboard')
def dashboard():
    """Nutrition tracking dashboard"""
    # Get or create default user (simplified for demo)
    user = User.query.first()
    if not user:
        user = User(username='demo_user')
        db.session.add(user)
        db.session.commit()
    
    return render_template('nutrition/dashboard.html', user=user)

@nutrition_bp.route('/api/log', methods=['POST'])
def log_meal():
    """Log a meal for today"""
    data = request.get_json()
    recipe_id = data.get('recipe_id')
    meal_type = data.get('meal_type', 'lunch')
    
    # Get default user
    user = User.query.first()
    
    # Create meal plan entry for today
    meal_plan = MealPlan(
        user_id=user.id,
        recipe_id=recipe_id,
        date=datetime.utcnow().date(),
        meal_type=meal_type
    )
    
    db.session.add(meal_plan)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'meal_plan': meal_plan.to_dict()
    })

@nutrition_bp.route('/api/stats')
def get_stats():
    """Get daily nutrition stats"""
    date_str = request.args.get('date', None)
    
    if date_str:
        target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    else:
        target_date = datetime.utcnow().date()
    
    # Get default user
    user = User.query.first()
    if not user:
        return jsonify({'error': 'No user found'}), 404
    
    # Get all meals for the date
    meals = MealPlan.query.filter_by(
        user_id=user.id,
        date=target_date
    ).all()
    
    # Calculate totals
    total_calories = sum(meal.recipe.calories for meal in meals if meal.recipe)
    total_protein = sum(meal.recipe.protein or 0 for meal in meals if meal.recipe)
    total_carbs = sum(meal.recipe.carbs or 0 for meal in meals if meal.recipe)
    total_fats = sum(meal.recipe.fats or 0 for meal in meals if meal.recipe)
    
    # Calculate remaining
    remaining_calories = user.calorie_goal - total_calories
    remaining_protein = user.protein_goal - total_protein
    remaining_carbs = user.carbs_goal - total_carbs
    remaining_fats = user.fats_goal - total_fats
    
    return jsonify({
        'date': target_date.isoformat(),
        'goals': {
            'calories': user.calorie_goal,
            'protein': user.protein_goal,
            'carbs': user.carbs_goal,
            'fats': user.fats_goal
        },
        'consumed': {
            'calories': total_calories,
            'protein': total_protein,
            'carbs': total_carbs,
            'fats': total_fats
        },
        'remaining': {
            'calories': remaining_calories,
            'protein': remaining_protein,
            'carbs': remaining_carbs,
            'fats': remaining_fats
        },
        'meals': [meal.to_dict() for meal in meals]
    })

@nutrition_bp.route('/api/weekly-stats')
def weekly_stats():
    """Get weekly nutrition trends"""
    user = User.query.first()
    if not user:
        return jsonify({'error': 'No user found'}), 404
    
    # Get last 7 days
    today = datetime.utcnow().date()
    week_data = []
    
    for i in range(7):
        date = today - timedelta(days=6-i)
        meals = MealPlan.query.filter_by(user_id=user.id, date=date).all()
        
        total_calories = sum(meal.recipe.calories for meal in meals if meal.recipe)
        
        week_data.append({
            'date': date.isoformat(),
            'calories': total_calories
        })
    
    return jsonify({'week_data': week_data})
