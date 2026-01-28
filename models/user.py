"""
User database model
"""
from models import db

class User(db.Model):
    """User model for storing user profile and goals"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    
    # Nutrition goals
    calorie_goal = db.Column(db.Float, default=2000)
    protein_goal = db.Column(db.Float, default=150)  # grams
    carbs_goal = db.Column(db.Float, default=200)  # grams
    fats_goal = db.Column(db.Float, default=65)  # grams
    
    # Relationships
    meal_plans = db.relationship('MealPlan', backref='user', lazy=True)
    
    def to_dict(self):
        """Convert user to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'calorie_goal': self.calorie_goal,
            'protein_goal': self.protein_goal,
            'carbs_goal': self.carbs_goal,
            'fats_goal': self.fats_goal
        }
    
    def __repr__(self):
        return f'<User {self.username}>'
