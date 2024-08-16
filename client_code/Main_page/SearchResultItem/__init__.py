from ._anvil_designer import SearchResultItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class SearchResultItem(SearchResultItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Set the data bindings
    self.result_label.text = self.item['Name']

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Abrufen der Rezeptdetails vom Server
    recipe_data = anvil.server.call('get_recipe_details', self.item['RecipeID'])
    open_form('RecipeCard', recipe_data=recipe_data, previous_page="Main_page")
