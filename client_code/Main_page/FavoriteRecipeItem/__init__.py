from ._anvil_designer import FavoriteRecipeItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class FavoriteRecipeItem(FavoriteRecipeItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Setze den Rezeptnamen und die Kategorie
    self.label_name.text = self.item['Name']
    self.label_category.text = self.item['Category']
    # Any code you write here will run before the form opens.
  def show_recipe_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    recipe_id = self.item['RecipeID']
    recipe_data = anvil.server.call('get_recipe_details', recipe_id)
    open_form('RecipeCard', recipe_data=recipe_data, previous_page="Main_page")

