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
    # Set the data bindings
    self.image_1.source = self.item['RecipePicture']
    self.label_name.text = self.item['Name']
    # Any code you write here will run before the form opens.

    # Debugging-Ausgabe
    print("Item in RecipeResultItem:", self.item)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('RecipeCard',recipe=self.item)
