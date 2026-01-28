"""
Configuration settings for EATR Health App
"""
import os

class Config:
    """Base configuration"""
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask configuration
    DEBUG = os.environ.get('FLASK_ENV') != 'production'
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 5000))
