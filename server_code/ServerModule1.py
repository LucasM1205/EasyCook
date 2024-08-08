import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def search_recipes(keyword):
    # Abrufen aller Rezepte
    all_recipes = app_tables.recipes.search(tables.order_by("Name"))
    
    # Filtern der Rezepte nach Keyword
    matching_recipes = [recipe for recipe in all_recipes if keyword.lower() in recipe['Name'].lower()]
    
    return matching_recipes

@anvil.server.callable
def add_ingredient(name, category, unit):
    app_tables.ingredients.add_row(Name=name, Category=category, Unit=unit)

@anvil.server.callable
def add_recipe(name, description, category, preparation_time):
    app_tables.recipes.add_row(Name=name, Description=description, Category=category, PreparationTime=preparation_time)

@anvil.server.callable
def add_recipe_ingredient(recipe_id, ingredient_id, quantity):
    recipe = app_tables.recipes.get(RecipeID=recipe_id)
    ingredient = app_tables.ingredients.get(IngredientID=ingredient_id)
    app_tables.recipeingredients.add_row(RecipeID=recipe, IngredientID=ingredient, Quantity=quantity)

@anvil.server.callable
def get_ingredients_for_recipe(recipe_id):
    # Hier holen wir die Zeile der Recipe-Tabelle
    recipe_row = app_tables.recipes.get(RecipeID=recipe_id)
    if not recipe_row:
        raise ValueError("Recipe not found")
    
    # Suche mit der Recipe-Zeile anstatt nur der ID
    recipe_ingredients = app_tables.recipeingredients.search(RecipeID=recipe_row)
    ingredients = []
    
    for recipe_ingredient in recipe_ingredients:
        ingredient = recipe_ingredient['IngredientID']
        ingredients.append({
            'name': ingredient['Name'],
            'quantity': recipe_ingredient['Quantity'],
            'unit': ingredient['Unit']
        })
    
    return ingredients

@anvil.server.callable
def get_all_ingredients():
    return [row['Name'] for row in app_tables.ingredients.search()]

@anvil.server.callable
def get_recipes_by_ingredients(selected_ingredients):
    matching_recipes = []
    for recipe in app_tables.recipes.search():
        ingredients = [ri['IngredientID']['Name'] for ri in app_tables.recipeingredients.search(RecipeID=recipe)]
        print(f"Recipe: {recipe['Name']}, Ingredients: {ingredients}")  # Debugging-Ausgabe
        match_count = sum(ingredient in ingredients for ingredient in selected_ingredients)
        if match_count > 0:
            matching_recipes.append({'recipe': recipe, 'match_count': match_count})
    
    # Sort by the number of matching ingredients, descending
    matching_recipes.sort(key=lambda x: x['match_count'], reverse=True)
    
    print(f"Matching Recipes: {matching_recipes}")  # Debugging-Ausgabe
    return [mr['recipe'] for mr in matching_recipes]

