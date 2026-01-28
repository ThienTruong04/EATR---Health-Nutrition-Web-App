"""
Entry point for Vercel deployment
"""
import sys/* File: static/css/style.css, dòng ~336 */
.page-header {
    background: var(--gradient-secondary);
    color: white;
    padding: var(--spacing-xl) 0;
    text-align: center;
}<!-- File: templates/about.html, dòng 5-10 -->
<section class="page-header">
    <div class="container">
        <h1>About EATR</h1>
        <p>Your personal culinary companion</p>
    </div>
</section>
import os

# Set working directory and add to path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Change to base directory for relative imports
os.chdir(BASE_DIR)

try:
    from app import create_app
    app = create_app()
except Exception as e:
    print(f"Error initializing app: {e}")
    import traceback
    traceback.print_exc()
    raise

# Vercel will call this app object
if __name__ == '__main__':
    app.run(debug=False)
<!-- File: templates/about.html, dòng 5-10 -->
<section class="page-header">
    <div class="container">
        <h1>About NUTRISCAN</h1>
        <p>Your personal culinary companion</p>
    </div>
</section>