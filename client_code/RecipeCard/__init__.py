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
  def __init__(self, recipe, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Setze die Daten für das ausgewählte Rezept
    self.image_1.source = recipe['RecipePicture']
    self.label_name.text = recipe['Name']
    self.label_ingredients.text = self.format_ingredients(recipe['Ingredients'])  # Nehme an, es gibt eine Liste der Zutaten
    #self.label_preparation.text = recipe['PreparationSteps']  # Nehme an, es gibt einen String mit den Zubereitungsschritten

  def format_ingredients(self, ingredients):
    return "\n".join([f"{ing['quantity']} {ing['unit']} {ing['name']}" for ing in ingredients])
    # Any code you write here will run before the form opens.
