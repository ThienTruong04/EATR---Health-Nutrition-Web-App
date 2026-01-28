"""
Meal Plan database model
"""
from models import db
from datetime import datetime

class MealPlan(db.Model):
    """Meal plan model for tracking planned meals"""
    __tablename__ = 'meal_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    meal_type = db.Column(db.String(20), nullable=False)  # breakfast, lunch, dinner
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert meal plan to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id,
            'recipe_name': self.recipe.name if self.recipe else None,
            'date': self.date.isoformat() if self.date else None,
            'meal_type': self.meal_type,
            'calories': self.recipe.calories if self.recipe else 0,
            'protein': self.recipe.protein if self.recipe else 0,
            'carbs': self.recipe.carbs if self.recipe else 0,
            'fats': self.recipe.fats if self.recipe else 0
        }
    
    def __repr__(self):
        return f'<MealPlan {self.meal_type} on {self.date}>'
