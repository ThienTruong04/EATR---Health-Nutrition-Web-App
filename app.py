"""
EATR Health App - Main Flask Application
"""
from flask import Flask
from config import Config
from models import db
from models.recipe import Recipe
from models.user import User
from models.meal_plan import MealPlan

def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    from routes.main import main_bp
    from routes.recipes import recipes_bp
    from routes.nutrition import nutrition_bp
    from routes.meal_planner import meal_planner_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(nutrition_bp)
    app.register_blueprint(meal_planner_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("🚀 Starting EATR Health App...")
    print("📍 Running on: http://localhost:5000")
    print("📚 API Docs: http://localhost:5000/api")
    print("\n💡 To seed the database, run:")
    print("   python -c \"from utils.seed_data import seed_database; from app import app; app.app_context().push(); seed_database()\"")
    print("\n")
    
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
