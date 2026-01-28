# 🥗 EATR - Health & Nutrition Web App

A modern, full-stack web application for healthy eating, meal planning, and nutrition tracking built with **Python/Flask** and inspired by the EATR platform.

## ✨ Features

- 📚 **Extensive Recipe Database** - Browse 20+ healthy recipes with full nutrition information
- 🔍 **Smart Search & Filters** - Find recipes by category, dietary tags, or keywords
- 📅 **Weekly Meal Planner** - Plan your meals for the entire week with a visual calendar
- 📊 **Nutrition Dashboard** - Track daily calories, macros (protein/carbs/fats), and progress
- 🎯 **Personalized Goals** - Set custom calorie and macro targets
- 📱 **Responsive Design** - Beautiful UI that works on desktop, tablet, and mobile
- 🎨 **Modern UI/UX** - Gradient designs, smooth animations, glassmorphism effects

## 🛠️ Tech Stack

### Backend

- **Python 3.8+**
- **Flask 3.0.0** - Lightweight web framework
- **Flask-SQLAlchemy 3.1.1** - ORM for database operations
- **SQLite** - Local database (no setup required)

### Frontend

- **HTML5** with Jinja2 templates
- **CSS3** with modern features (Grid, Flexbox, CSS Variables)
- **Vanilla JavaScript** (ES6+)
- **Chart.js 4.4.0** - For nutrition visualizations

### Design

- Google Fonts (Inter & Outfit)
- Custom gradient color palette
- Responsive mobile-first design
- Smooth animations and transitions

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory:**

   ```bash
   cd C:\Users\duc90\.gemini\antigravity\scratch\eatr-health-app
   ```

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Seed the database with sample data:**

   ```bash
   python -c "from utils.seed_data import seed_database; from app import app; app.app_context().push(); seed_database()"
   ```

4. **Run the Flask development server:**

   ```bash
   python app.py
   ```

5. **Open your browser and visit:**

   ```
   http://localhost:5000
   ```

## 🚀 Usage

### Homepage

- View featured recipes
- Learn about the app's three-step process
- Quick access to all major features

### Recipe Browser (`/recipes`)

- Browse all available recipes
- Filter by category (Breakfast, Lunch, Dinner, Snacks)
- Filter by dietary tags (Vegetarian, Vegan, Gluten-Free, etc.)
- Search recipes by name or description
- Click on any recipe for detailed view

### Recipe Detail (`/recipes/<id>`)

- Full recipe information with large image
- Complete nutrition facts panel
- Ingredient list and step-by-step instructions
- Add recipe directly to meal plan

### Meal Planner (`/meal-planner`)

- View weekly calendar (Monday - Sunday)
- Add recipes to breakfast, lunch, or dinner slots
- See daily calorie totals
- Remove meals from plan
- Persistent storage in database

### Nutrition Dashboard (`/nutrition/dashboard`)

- Track today's calorie intake
- Visualize macro breakdown with pie chart
- See weekly calorie trends
- View meal log history
- Monitor progress toward goals

## 📁 Project Structure

```
eatr-health-app/
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── database.db                 # SQLite database (auto-created)
│
├── models/                     # Database models
│   ├── __init__.py            # Database initialization
│   ├── recipe.py              # Recipe model
│   ├── user.py                # User model
│   └── meal_plan.py           # Meal plan model
│
├── routes/                     # Flask blueprints/routes
│   ├── __init__.py
│   ├── main.py                # Homepage routes
│   ├── recipes.py             # Recipe routes + APIs
│   ├── nutrition.py           # Nutrition tracking routes
│   └── meal_planner.py        # Meal planner routes
│
├── utils/                      # Utility functions
│   ├── __init__.py
│   ├── nutrition_calc.py      # Nutrition calculations
│   └── seed_data.py           # Database seeding script
│
├── static/                     # Static assets
│   ├── css/
│   │   ├── style.css          # Main styles
│   │   └── responsive.css     # Responsive + component styles
│   ├── js/
│   │   ├── app.js             # Main JavaScript
│   │   └── charts.js          # Chart.js visualizations
│   └── images/
│       └── placeholder.jpg    # Placeholder recipe image
│
└── templates/                  # Jinja2 templates
    ├── base.html              # Base template
    ├── index.html             # Homepage
    ├── about.html             # About page
    ├── recipes/
    │   ├── browse.html        # Recipe browsing
    │   └── detail.html        # Recipe detail
    ├── nutrition/
    │   └── dashboard.html     # Nutrition dashboard
    └── meal_planner/
        └── planner.html       # Weekly meal planner
```

## 🔌 API Endpoints

### Recipes

- `GET /recipes` - Browse recipes with pagination
- `GET /recipes/<id>` - Get recipe details
- `GET /recipes/api/search?q=<query>` - Search recipes (JSON)
- `GET /recipes/api/filter?category=<cat>&tags=<tag>` - Filter recipes (JSON)

### Nutrition

- `GET /nutrition/dashboard` - Nutrition tracking page
- `POST /nutrition/api/log` - Log a meal
- `GET /nutrition/api/stats?date=<YYYY-MM-DD>` - Get daily stats (JSON)
- `GET /nutrition/api/weekly-stats` - Get 7-day trends (JSON)

### Meal Planner

- `GET /meal-planner` - Weekly planner page
- `POST /meal-planner/api/add` - Add recipe to plan
- `DELETE /meal-planner/api/remove/<id>` - Remove from plan
- `GET /meal-planner/api/week` - Get current week plan (JSON)

## 🎨 Design Highlights

- **Color Palette**: Green primary (#10b981) with purple/blue gradients
- **Typography**: Inter (body), Outfit (headings)
- **Effects**: Glassmorphism, smooth transitions, hover animations
- **Responsive**: Mobile-first design with breakpoints at 768px and 1024px

## 📊 Database Schema

### Recipe

- `id`, `name`, `description`, `image_url`, `category`
- `prep_time`, `cook_time`, `servings`
- `calories`, `protein`, `carbs`, `fats`, `fiber`
- `ingredients` (JSON), `instructions` (JSON), `tags` (JSON)

### User

- `id`, `username`
- `calorie_goal`, `protein_goal`, `carbs_goal`, `fats_goal`

### MealPlan

- `id`, `user_id`, `recipe_id`
- `date`, `meal_type` (breakfast/lunch/dinner)

## 🔮 Future Enhancements

- User authentication and multi-user support
- Grocery list generator from meal plans
- Recipe favorites and ratings
- Mobile app (React Native or Flutter)
- Cloud deployment (Heroku, AWS, or Google Cloud)
- Advanced analytics and AI-powered recommendations
- PDF export for meal plans
- Integration with fitness trackers
- Social features (share recipes, meal plans)

## 🐛 Troubleshooting

**Database not seeding:**

```bash
# Make sure you're in the project directory
cd C:\Users\duc90\.gemini\antigravity\scratch\eatr-health-app

# Try running seed script directly
python utils/seed_data.py
```

**Port 5000 already in use:**

- Change the PORT in `config.py` to a different number (e.g., 5001)

**Module not found errors:**

- Ensure all dependencies are installed: `pip install -r requirements.txt`

## 📝 License

This project is for educational and demonstration purposes.

## 👨‍💻 Author

Built with ❤️ using Python, Flask, and modern web technologies.

---

**Note:** This is a demo application with sample data. In production, you would want to add:

- User authentication
- Input validation and sanitization
- CSRF protection
- Rate limiting
- Environment-based configuration
- Production-grade database (PostgreSQL)
- Proper error handling and logging
