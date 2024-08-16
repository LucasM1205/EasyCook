from ._anvil_designer import RecipeCardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RecipeCard(RecipeCardTemplate):
  def __init__(self, recipe_data, previous_page, selected_ingredients=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Entpacken des Row-Objekts und der Details
    self.recipe = recipe_data['recipe']
    details = recipe_data['details']
    self.previous_page = previous_page
    self.selected_ingredients = selected_ingredients
    
    # Setze die Daten für das ausgewählte Rezept
    self.image_1.source = details['RecipePicture']
    self.label_name.text = details['Name']
    self.label_ingredients.text = self.format_ingredients(details['Ingredients'])
    self.label_preparation.text = details['PreparationSteps']

    # Überprüfe, ob das Rezept bereits ein Favorit ist
    self.update_favorite_status()
  
  def format_ingredients(self, ingredients):
    return "\n".join([f"{ing['quantity']} {ing['unit']} {ing['name']}" for ing in ingredients])
  
  def back_button_click(self, **event_args):
    """Zurück zur vorherigen Seite"""
    if self.previous_page == "Main_page":
        open_form('Main_page')
    elif self.previous_page == "RecipeResultsPage":
        open_form('RecipeResultsPage', selected_ingredients=self.selected_ingredients)

  def update_favorite_status(self):
    # Überprüfen, ob das Rezept bereits als Favorit markiert ist
    is_favorite = anvil.server.call('is_favorite', self.recipe)
    self.radio_button_favorite.selected = is_favorite

  def radio_button_favorite_change(self, **event_args):
    """Wird aufgerufen, wenn der RadioButton geändert wird"""
    if self.radio_button_favorite.selected:
      # Füge das Rezept zu den Favoriten hinzu
      anvil.server.call('add_to_favorites', self.recipe)

    else:
      # Entferne das Rezept aus den Favoriten
      anvil.server.call('remove_from_favorites', self.recipe)

    # Aktualisiere den Favoriten-Status
    self.update_favorite_status()
