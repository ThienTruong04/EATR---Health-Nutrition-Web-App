"""
Entry point for Vercel deployment
"""
import sys
import os

# Add parent directory to path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app

app = create_app()

# Vercel will call this app object
if __name__ == '__main__':
    app.run(debug=False)
