from ._anvil_designer import RecipeResultsPageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RecipeResultsPage(RecipeResultsPageTemplate):
  def __init__(self, selected_ingredients, **properties):
    # Pass **properties to self.init_components() before doing anything else
    self.init_components(**properties)
    
    # Debugging-Ausgabe
    print("Selected Ingredients in RecipeResultsPage:", selected_ingredients)
    
    # Load recipes based on selected ingredients
    recipes = anvil.server.call('get_recipes_by_ingredients', selected_ingredients)
    
    # Debugging-Ausgabe
    print("Recipes loaded in RecipeResultsPage:", recipes)
    
    # Display the recipes
    self.repeating_panel_1.items = recipes

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Main_page')
