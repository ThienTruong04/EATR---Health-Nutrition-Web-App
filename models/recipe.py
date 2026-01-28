"""
Recipe database model
"""
from models import db
import json

class Recipe(db.Model):
    """Recipe model for storing recipe information"""
    __tablename__ = 'recipes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500))
    category = db.Column(db.String(50))  # Breakfast, Lunch, Dinner, Snacks
    prep_time = db.Column(db.Integer)  # in minutes
    cook_time = db.Column(db.Integer)  # in minutes
    servings = db.Column(db.Integer, default=1)
    
    # Nutrition information (per serving)
    calories = db.Column(db.Float, nullable=False)
    protein = db.Column(db.Float)  # in grams
    carbs = db.Column(db.Float)  # in grams
    fats = db.Column(db.Float)  # in grams
    fiber = db.Column(db.Float)  # in grams
    
    # JSON fields
    ingredients_json = db.Column(db.Text)  # Stored as JSON string
    instructions_json = db.Column(db.Text)  # Stored as JSON string
    tags_json = db.Column(db.Text)  # Stored as JSON string
    
    # Relationships
    meal_plans = db.relationship('MealPlan', backref='recipe', lazy=True)
    
    @property
    def ingredients(self):
        """Get ingredients as Python list"""
        if self.ingredients_json:
            return json.loads(self.ingredients_json)
        return []
    
    @ingredients.setter
    def ingredients(self, value):
        """Set ingredients from Python list"""
        self.ingredients_json = json.dumps(value)
    
    @property
    def instructions(self):
        """Get instructions as Python list"""
        if self.instructions_json:
            return json.loads(self.instructions_json)
        return []
    
    @instructions.setter
    def instructions(self, value):
        """Set instructions from Python list"""
        self.instructions_json = json.dumps(value)
    
    @property
    def tags(self):
        """Get tags as Python list"""
        if self.tags_json:
            return json.loads(self.tags_json)
        return []
    
    @tags.setter
    def tags(self, value):
        """Set tags from Python list"""
        self.tags_json = json.dumps(value)
    
    @property
    def total_time(self):
        """Calculate total cooking time"""
        return (self.prep_time or 0) + (self.cook_time or 0)
    
    def to_dict(self):
        """Convert recipe to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url,
            'category': self.category,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'total_time': self.total_time,
            'servings': self.servings,
            'calories': self.calories,
            'protein': self.protein,
            'carbs': self.carbs,
            'fats': self.fats,
            'fiber': self.fiber,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'tags': self.tags
        }
    
    def __repr__(self):
        return f'<Recipe {self.name}>'
