from ._anvil_designer import Ingredient_Selection_Page_copyTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Ingredient_Selection_Page_copy(Ingredient_Selection_Page_copyTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    # Load the ingredients from the server
    ingredients = anvil.server.call('get_all_ingredients')
    
    # Debugging-Ausgabe
    print("Ingredients loaded:", ingredients)
    
    # Set the repeating panel items
    self.repeating_panel_1.items = [{'ingredient': ingredient, 'selected': True} for ingredient in ingredients]

  def link_1_click(self, **event_args):
    open_form("Main_page")

  def continue_click(self, **event_args):
    # Get selected ingredients
    selected_ingredients = [item['ingredient'] for item in self.repeating_panel_1.items if item['selected']]    
    
    # Debugging-Ausgabe
    print("Selected Ingredients:", selected_ingredients)
    
    # Pass selected ingredients to the next page
    open_form('RecipeResultsPage', selected_ingredients=selected_ingredients)
