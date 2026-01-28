"""
Database seeding script with sample recipes
"""
from models import db
from models.recipe import Recipe
from models.user import User

def seed_database():
    """Seed database with sample data"""
    print("Seeding database...")
    
    # Create tables
    db.create_all()
    
    # Check if already seeded
    if Recipe.query.first():
        print("Warning: Database already contains data. Skipping seed.")
        return
    
    # Create default user
    user = User(
        username='demo_user',
        calorie_goal=2000,
        protein_goal=150,
        carbs_goal=200,
        fats_goal=65
    )
    db.session.add(user)
    
    # Sample recipes data
    recipes_data = [
        {
            'name': 'Avocado Toast with Poached Eggs',
            'description': 'A healthy and delicious breakfast with whole grain toast, creamy avocado, and perfectly poached eggs.',
            'category': 'Breakfast',
            'prep_time': 5,
            'cook_time': 10,
            'servings': 1,
            'calories': 380,
            'protein': 18,
            'carbs': 35,
            'fats': 20,
            'fiber': 12,
            'ingredients': [
                '2 slices whole grain bread',
                '1 ripe avocado',
                '2 eggs',
                'Salt and pepper to taste',
                'Red pepper flakes (optional)'
            ],
            'instructions': [
                'Toast the bread until golden brown',
                'Mash avocado with salt and pepper',
                'Poach eggs in simmering water for 3-4 minutes',
                'Spread avocado on toast and top with poached eggs',
                'Garnish with red pepper flakes'
            ],
            'tags': ['Vegetarian', 'High-Protein', 'Healthy-Fats'],
            'image_url': '/static/images/avocado-toast.jpg'
        },
        {
            'name': 'Greek Yogurt Parfait',
            'description': 'Creamy Greek yogurt layered with fresh berries, granola, and a drizzle of honey.',
            'category': 'Breakfast',
            'prep_time': 5,
            'cook_time': 0,
            'servings': 1,
            'calories': 320,
            'protein': 20,
            'carbs': 45,
            'fats': 8,
            'fiber': 6,
            'ingredients': [
                '1 cup Greek yogurt',
                '1/2 cup mixed berries',
                '1/4 cup granola',
                '1 tbsp honey',
                'Mint leaves for garnish'
            ],
            'instructions': [
                'Layer Greek yogurt in a glass',
                'Add mixed berries',
                'Top with granola',
                'Drizzle with honey',
                'Garnish with mint leaves'
            ],
            'tags': ['Vegetarian', 'High-Protein', 'Gluten-Free'],
            'image_url': '/static/images/greek-yogurt-parfait.jpg'
        },
        {
            'name': 'Grilled Chicken Salad',
            'description': 'Fresh mixed greens topped with grilled chicken breast, cherry tomatoes, cucumber, and balsamic vinaigrette.',
            'category': 'Lunch',
            'prep_time': 15,
            'cook_time': 15,
            'servings': 1,
            'calories': 420,
            'protein': 45,
            'carbs': 25,
            'fats': 15,
            'fiber': 8,
            'ingredients': [
                '6 oz chicken breast',
                '4 cups mixed greens',
                '1 cup cherry tomatoes',
                '1/2 cucumber, sliced',
                '2 tbsp balsamic vinaigrette',
                'Salt and pepper to taste'
            ],
            'instructions': [
                'Season chicken with salt and pepper',
                'Grill chicken for 6-7 minutes per side',
                'Let chicken rest for 5 minutes, then slice',
                'Arrange greens on plate',
                'Top with tomatoes, cucumber, and chicken',
                'Drizzle with vinaigrette'
            ],
            'tags': ['High-Protein', 'Low-Carb', 'Gluten-Free', 'Diabetes-Friendly'],
            'image_url': '/static/images/grilled-chicken-salad.jpg'
        },
        {
            'name': 'Quinoa Buddha Bowl',
            'description': 'Nutritious bowl with quinoa, roasted vegetables, chickpeas, and tahini dressing.',
            'category': 'Lunch',
            'prep_time': 15,
            'cook_time': 30,
            'servings': 1,
            'calories': 480,
            'protein': 18,
            'carbs': 65,
            'fats': 16,
            'fiber': 14,
            'ingredients': [
                '1/2 cup quinoa',
                '1 cup mixed roasted vegetables',
                '1/2 cup chickpeas',
                '2 cups spinach',
                '2 tbsp tahini dressing',
                'Lemon wedge'
            ],
            'instructions': [
                'Cook quinoa according to package instructions',
                'Roast vegetables at 400°F for 25 minutes',
                'Arrange quinoa, vegetables, and chickpeas in bowl',
                'Add fresh spinach',
                'Drizzle with tahini dressing',
                'Serve with lemon wedge'
            ],
            'tags': ['Vegan', 'Vegetarian', 'High-Fiber', 'Gluten-Free'],
            'image_url': '/static/images/quinoa-buddha-bowl.jpg'
        },
        {
            'name': 'Baked Salmon with Asparagus',
            'description': 'Omega-3 rich salmon fillet baked with fresh asparagus and lemon herb seasoning.',
            'category': 'Dinner',
            'prep_time': 10,
            'cook_time': 20,
            'servings': 1,
            'calories': 450,
            'protein': 42,
            'carbs': 12,
            'fats': 26,
            'fiber': 5,
            'ingredients': [
                '6 oz salmon fillet',
                '1 cup asparagus spears',
                '1 tbsp olive oil',
                '1 lemon',
                'Fresh dill',
                'Salt and pepper to taste'
            ],
            'instructions': [
                'Preheat oven to 400°F',
                'Place salmon and asparagus on baking sheet',
                'Drizzle with olive oil',
                'Season with salt, pepper, and dill',
                'Add lemon slices',
                'Bake for 18-20 minutes'
            ],
            'tags': ['High-Protein', 'Low-Carb', 'Gluten-Free', 'Healthy-Fats', 'Diabetes-Friendly'],
            'image_url': '/static/images/baked-salmon.jpg'
        },
        {
            'name': 'Turkey Meatballs with Zucchini Noodles',
            'description': 'Lean turkey meatballs served over spiralized zucchini with marinara sauce.',
            'category': 'Dinner',
            'prep_time': 20,
            'cook_time': 25,
            'servings': 1,
            'calories': 420,
            'protein': 38,
            'carbs': 28,
            'fats': 18,
            'fiber': 8,
            'ingredients': [
                '6 oz ground turkey',
                '2 medium zucchinis, spiralized',
                '1 cup marinara sauce',
                '1 egg',
                '1/4 cup breadcrumbs',
                'Italian herbs',
                'Parmesan cheese'
            ],
            'instructions': [
                'Mix turkey, egg, breadcrumbs, and herbs',
                'Form into meatballs',
                'Bake at 375°F for 20-25 minutes',
                'Sauté zucchini noodles for 2-3 minutes',
                'Heat marinara sauce',
                'Serve meatballs over zucchini noodles',
                'Top with parmesan'
            ],
            'tags': ['High-Protein', 'Low-Carb', 'Diabetes-Friendly'],
            'image_url': '/static/images/turkey-meatballs.jpg'
        },
        {
            'name': 'Veggie Stir-Fry with Tofu',
            'description': 'Colorful vegetable stir-fry with crispy tofu in a savory soy-ginger sauce.',
            'category': 'Dinner',
            'prep_time': 15,
            'cook_time': 15,
            'servings': 1,
            'calories': 380,
            'protein': 22,
            'carbs': 35,
            'fats': 18,
            'fiber': 10,
            'ingredients': [
                '6 oz firm tofu',
                '2 cups mixed vegetables (broccoli, bell peppers, carrots)',
                '2 tbsp soy sauce',
                '1 tsp ginger, minced',
                '2 cloves garlic, minced',
                '1 tbsp sesame oil',
                '1/2 cup brown rice (cooked)'
            ],
            'instructions': [
                'Press and cube tofu',
                'Sauté tofu in sesame oil until golden',
                'Remove tofu and set aside',
                'Stir-fry vegetables with garlic and ginger',
                'Add soy sauce',
                'Return tofu to pan',
                'Serve over brown rice'
            ],
            'tags': ['Vegan', 'Vegetarian', 'High-Protein', 'Diabetes-Friendly'],
            'image_url': '/static/images/veggie-stir-fry.jpg'
        },
        {
            'name': 'Protein Smoothie Bowl',
            'description': 'Thick and creamy smoothie bowl topped with fresh fruits, nuts, and seeds.',
            'category': 'Breakfast',
            'prep_time': 10,
            'cook_time': 0,
            'servings': 1,
            'calories': 420,
            'protein': 28,
            'carbs': 52,
            'fats': 14,
            'fiber': 12,
            'ingredients': [
                '1 scoop protein powder',
                '1 banana',
                '1/2 cup frozen berries',
                '1/2 cup almond milk',
                'Toppings: granola, sliced fruits, chia seeds'
            ],
            'instructions': [
                'Blend protein powder, banana, berries, and almond milk',
                'Pour into bowl',
                'Top with granola, sliced fruits, and chia seeds',
                'Enjoy immediately'
            ],
            'tags': ['Vegetarian', 'High-Protein', 'Gluten-Free'],
            'image_url': '/static/images/protein-smoothie-bowl.jpg'
        },
        {
            'name': 'Chickpea Mediterranean Wrap',
            'description': 'Whole wheat wrap filled with seasoned chickpeas, fresh vegetables, and tzatziki sauce.',
            'category': 'Lunch',
            'prep_time': 10,
            'cook_time': 10,
            'servings': 1,
            'calories': 450,
            'protein': 16,
            'carbs': 62,
            'fats': 15,
            'fiber': 14,
            'ingredients': [
                '1 whole wheat tortilla',
                '3/4 cup chickpeas',
                'Lettuce, tomatoes, cucumber',
                '3 tbsp tzatziki sauce',
                'Red onion',
                'Mediterranean spices'
            ],
            'instructions': [
                'Season and sauté chickpeas',
                'Warm tortilla',
                'Layer lettuce, tomatoes, cucumber',
                'Add chickpeas',
                'Drizzle with tzatziki',
                'Wrap and serve'
            ],
            'tags': ['Vegetarian', 'High-Fiber', 'Diabetes-Friendly'],
            'image_url': '/static/images/chickpea-wrap.jpg'
        },
        {
            'name': 'Overnight Oats with Berries',
            'description': 'Convenient and nutritious overnight oats with mixed berries and almond butter.',
            'category': 'Breakfast',
            'prep_time': 5,
            'cook_time': 0,
            'servings': 1,
            'calories': 380,
            'protein': 14,
            'carbs': 52,
            'fats': 14,
            'fiber': 10,
            'ingredients': [
                '1/2 cup rolled oats',
                '1/2 cup almond milk',
                '1 tbsp chia seeds',
                '1/2 cup mixed berries',
                '1 tbsp almond butter',
                'Honey to taste'
            ],
            'instructions': [
                'Mix oats, almond milk, and chia seeds in jar',
                'Refrigerate overnight',
                'In the morning, top with berries',
                'Add almond butter',
                'Drizzle with honey'
            ],
            'tags': ['Vegan', 'Vegetarian', 'High-Fiber', 'Gluten-Free'],
            'image_url': '/static/images/overnight-oats.jpg'
        }
    ]
    
    # Add recipes to database
    for recipe_data in recipes_data:
        recipe = Recipe(
            name=recipe_data['name'],
            description=recipe_data['description'],
            category=recipe_data['category'],
            prep_time=recipe_data['prep_time'],
            cook_time=recipe_data['cook_time'],
            servings=recipe_data['servings'],
            calories=recipe_data['calories'],
            protein=recipe_data['protein'],
            carbs=recipe_data['carbs'],
            fats=recipe_data['fats'],
            fiber=recipe_data['fiber'],
            image_url=recipe_data['image_url']
        )
        
        # Set JSON fields using properties
        recipe.ingredients = recipe_data['ingredients']
        recipe.instructions = recipe_data['instructions']
        recipe.tags = recipe_data['tags']
        
        db.session.add(recipe)
    
    # Commit all changes
    db.session.commit()
    
    print(f"Successfully seeded {len(recipes_data)} recipes and 1 user!")
    print("Database is ready to use!")

if __name__ == '__main__':
    from app import app
    with app.app_context():
        seed_database()
