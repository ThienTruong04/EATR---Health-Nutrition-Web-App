"""
Seed database script - Run this to populate the database
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from utils.seed_data import seed_database

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_database()
