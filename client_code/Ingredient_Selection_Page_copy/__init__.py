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
    #print("Ingredients loaded:", ingredients)
    # Set the repeating panel items
    self.repeating_panel_1.items = [{'ingredient': ingredient, 'selected': True} for ingredient in ingredients]
    # Debugging-Ausgabe um zu überprüfen, ob alle Items korrekt geladen wurden
    print(f"Ingredients loaded: {ingredients}")
  
  def update_selection(self):
    # This method updates the selected ingredients based on the checkboxes
    selected_ingredients = [item['ingredient'] for item in self.repeating_panel_1.items if item['selected']]
    print("Currently selected ingredients:", selected_ingredients)
  
  def link_1_click(self, **event_args):
    open_form("Main_page")

  def continue_click(self, **event_args):

    for item in self.repeating_panel_1.items:
      print(f"Item: {item['ingredient']}, Selected: {item['selected']}")
    
    # Get selected ingredients
    selected_ingredients = [item['ingredient'] for item in self.repeating_panel_1.items if item['selected']]    
    # Debugging-Ausgabe
    #print("Selected Ingredients:", selected_ingredients)
    print(f"Selected Ingredients before moving to next page: {selected_ingredients}")
    # Pass selected ingredients to the next page
    open_form('RecipeResultsPage', selected_ingredients=selected_ingredients)
