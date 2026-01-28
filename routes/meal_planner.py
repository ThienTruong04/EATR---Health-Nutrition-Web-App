"""
Meal planner routes
"""
from flask import Blueprint, render_template, jsonify, request
from models import db
from models.user import User
from models.meal_plan import MealPlan
from models.recipe import Recipe
from datetime import datetime, timedelta

meal_planner_bp = Blueprint('meal_planner', __name__, url_prefix='/meal-planner')

@meal_planner_bp.route('/')
def planner():
    """Weekly meal planner view"""
    user = User.query.first()
    if not user:
        user = User(username='demo_user')
        db.session.add(user)
        db.session.commit()
    
    return render_template('meal_planner/planner.html', user=user)

@meal_planner_bp.route('/api/add', methods=['POST'])
def add_to_plan():
    """Add recipe to meal plan"""
    data = request.get_json()
    recipe_id = data.get('recipe_id')
    date_str = data.get('date')
    meal_type = data.get('meal_type')
    
    # Parse date
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    # Get default user
    user = User.query.first()
    
    # Check if meal already exists for this slot
    existing = MealPlan.query.filter_by(
        user_id=user.id,
        date=date,
        meal_type=meal_type
    ).first()
    
    if existing:
        # Update existing
        existing.recipe_id = recipe_id
        db.session.commit()
        return jsonify({
            'success': True,
            'meal_plan': existing.to_dict()
        })
    else:
        # Create new
        meal_plan = MealPlan(
            user_id=user.id,
            recipe_id=recipe_id,
            date=date,
            meal_type=meal_type
        )
        db.session.add(meal_plan)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'meal_plan': meal_plan.to_dict()
        })

@meal_planner_bp.route('/api/remove/<int:meal_plan_id>', methods=['DELETE'])
def remove_from_plan(meal_plan_id):
    """Remove meal from plan"""
    meal_plan = MealPlan.query.get_or_404(meal_plan_id)
    db.session.delete(meal_plan)
    db.session.commit()
    
    return jsonify({'success': True})

@meal_planner_bp.route('/api/week')
def get_week():
    """Get meal plan for current week"""
    user = User.query.first()
    if not user:
        return jsonify({'error': 'No user found'}), 404
    
    # Get start of week (Monday)
    today = datetime.utcnow().date()
    start_of_week = today - timedelta(days=today.weekday())
    
    # Get 7 days starting from Monday
    week_plan = {}
    for i in range(7):
        date = start_of_week + timedelta(days=i)
        meals = MealPlan.query.filter_by(
            user_id=user.id,
            date=date
        ).all()
        
        # Calculate daily totals
        daily_calories = sum(meal.recipe.calories for meal in meals if meal.recipe)
        daily_protein = sum(meal.recipe.protein or 0 for meal in meals if meal.recipe)
        daily_carbs = sum(meal.recipe.carbs or 0 for meal in meals if meal.recipe)
        daily_fats = sum(meal.recipe.fats or 0 for meal in meals if meal.recipe)
        
        week_plan[date.isoformat()] = {
            'date': date.isoformat(),
            'day_name': date.strftime('%A'),
            'meals': {
                'breakfast': next((m.to_dict() for m in meals if m.meal_type == 'breakfast'), None),
                'lunch': next((m.to_dict() for m in meals if m.meal_type == 'lunch'), None),
                'dinner': next((m.to_dict() for m in meals if m.meal_type == 'dinner'), None)
            },
            'totals': {
                'calories': daily_calories,
                'protein': daily_protein,
                'carbs': daily_carbs,
                'fats': daily_fats
            }
        }
    
    return jsonify({
        'week_plan': week_plan,
        'start_date': start_of_week.isoformat()
    })
