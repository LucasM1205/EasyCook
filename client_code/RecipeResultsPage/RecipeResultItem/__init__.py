from ._anvil_designer import RecipeResultItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RecipeResultItem(RecipeResultItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.source = self.item['RecipePicture']
    self.label_name.text = self.item['Name']
    # Debugging-Ausgabe
    print("Item in RecipeResultItem:", self.item)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    recipe_id = self.item['RecipeID']
    recipe_data = anvil.server.call('get_recipe_details', recipe_id)
    # Hole die aktuelle Instanz der geöffneten Form (RecipeResultsPage)
    parent_form = get_open_form()
    open_form('RecipeCard', recipe_data=recipe_data, previous_page="RecipeResultsPage", selected_ingredients=parent_form.selected_ingredients)