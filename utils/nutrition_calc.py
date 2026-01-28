"""
Nutrition calculation utilities
"""

def calculate_macros_percentage(protein, carbs, fats):
    """
    Calculate the percentage distribution of macronutrients
    
    Args:
        protein: Protein in grams
        carbs: Carbs in grams
        fats: Fats in grams
    
    Returns:
        Dictionary with percentages for each macro
    """
    # Calories per gram: Protein=4, Carbs=4, Fats=9
    protein_cals = protein * 4
    carbs_cals = carbs * 4
    fats_cals = fats * 9
    
    total_cals = protein_cals + carbs_cals + fats_cals
    
    if total_cals == 0:
        return {'protein': 0, 'carbs': 0, 'fats': 0}
    
    return {
        'protein': round((protein_cals / total_cals) * 100, 1),
        'carbs': round((carbs_cals / total_cals) * 100, 1),
        'fats': round((fats_cals / total_cals) * 100, 1)
    }

def calculate_daily_remaining(consumed, goals):
    """
    Calculate remaining macros and calories for the day
    
    Args:
        consumed: Dictionary with consumed values
        goals: Dictionary with goal values
    
    Returns:
        Dictionary with remaining values
    """
    return {
        'calories': goals.get('calories', 0) - consumed.get('calories', 0),
        'protein': goals.get('protein', 0) - consumed.get('protein', 0),
        'carbs': goals.get('carbs', 0) - consumed.get('carbs', 0),
        'fats': goals.get('fats', 0) - consumed.get('fats', 0)
    }

def calculate_calories_from_macros(protein, carbs, fats):
    """
    Calculate total calories from macronutrients
    
    Args:
        protein: Protein in grams
        carbs: Carbs in grams
        fats: Fats in grams
    
    Returns:
        Total calories
    """
    return (protein * 4) + (carbs * 4) + (fats * 9)

def get_macro_color(macro_type):
    """
    Get color code for macro type for visualization
    
    Args:
        macro_type: 'protein', 'carbs', or 'fats'
    
    Returns:
        Hex color code
    """
    colors = {
        'protein': '#FF6384',  # Red/Pink
        'carbs': '#36A2EB',    # Blue
        'fats': '#FFCE56'      # Yellow
    }
    return colors.get(macro_type, '#999999')
