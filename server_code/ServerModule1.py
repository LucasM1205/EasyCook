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

@anvil.server.callable
def get_recipe_details(recipe_id):
    # Rezept abrufen
    recipe = app_tables.recipes.get(RecipeID=recipe_id)
    if recipe is None:
        raise ValueError(f"Recipe with ID {recipe_id} not found.")
    
    # Debugging: Direkt auf das Feld zugreifen
    print("Recipe Name:", recipe['Name'])
    print("PreparationSteps Field:", recipe['PreparationSteps'])
    
    # Zutaten und Mengen über die Assoziationstabelle abrufen
    ingredients = []
    for ri in app_tables.recipeingredients.search(RecipeID=recipe):
        ingredient = ri['IngredientID']
        ingredients.append({
            'name': ingredient['Name'],
            'quantity': ri['Quantity'],
            'unit': ingredient['Unit']
        })
    
    # Rezeptdetails zusammenstellen und das vollständige Row-Objekt zurückgeben
    return {
        'recipe': recipe,
        'details': {
            'Name': recipe['Name'],
            'RecipePicture': recipe['RecipePicture'],
            'Ingredients': ingredients,
            'PreparationSteps': recipe['PreparationSteps']  # Direktes Feld, ohne get()
        }
    }
  
@anvil.server.callable
def is_favorite(recipe):
    user = anvil.users.get_user()
    # Direktes Verwenden des Row-Objekts
    return app_tables.favorites.get(user=user, recipe=recipe) is not None

@anvil.server.callable
def add_to_favorites(recipe):
    user = anvil.users.get_user()
    if not app_tables.favorites.get(user=user, recipe=recipe):
        app_tables.favorites.add_row(user=user, recipe=recipe)
        #Aktualisieren der Favoritenanzahl
        if 'FavoritesCount' in recipe:
            recipe['FavoritesCount'] += 1
        else:
            recipe['FavoritesCount'] = 1
        #recipe.save()

@anvil.server.callable
def remove_from_favorites(recipe):
    user = anvil.users.get_user()
    favorite_row = app_tables.favorites.get(user=user, recipe=recipe)
    if favorite_row:
        favorite_row.delete()
        #Aktualisieren der Favoritenanzahl
        if 'FavoritesCount' in recipe:
          recipe['FavoritesCount'] = max(0, recipe['FavoritesCount'] - 1)
        else:
          recipe['FavoritesCount'] = 0
        #recipe.save()

@anvil.server.callable
def get_popular_recipes(limit=3):
    # Abrufen der Rezepte mit den höchsten FavoritesCount
    popular_recipes = list(app_tables.recipes.search(tables.order_by("FavoritesCount", ascending=False)))
    # Begrenzen der Anzahl der Ergebnisse
    return popular_recipes[:limit]
    # Konvertiere die Ergebnisse in eine Liste von Dictionaries
    return [{'RecipeID': recipe['RecipeID'], 'RecipePicture': recipe['RecipePicture']} for recipe in popular_recipes]


@anvil.server.callable
def get_favorite_recipes():
    user = anvil.users.get_user()
    if user is None:
        return []
    favorite_rows = app_tables.favorites.search(user=user)
    favorite_recipes = [fav['recipe'] for fav in favorite_rows] 
    return favorite_recipes

@anvil.server.callable
def add_comment(recipe_id, comment_text):
    user = anvil.users.get_user()
    if user is None:
        raise ValueError("User must be logged in to comment.")
    
    recipe = app_tables.recipes.get(RecipeID=recipe_id)
    if recipe is None:
        raise ValueError(f"Recipe with ID {recipe_id} not found.")
    
    app_tables.comments.add_row(
        Recipe=recipe,
        User=user,
        CommentText=comment_text,
        Timestamp=datetime.now()
    )

@anvil.server.callable
def get_comments_for_recipe(recipe_id):
    recipe = app_tables.recipes.get(RecipeID=recipe_id)
    if recipe is None:
        raise ValueError(f"Recipe with ID {recipe_id} not found.")
    
    return app_tables.comments.search(tables.order_by('Timestamp', ascending=False), Recipe=recipe)