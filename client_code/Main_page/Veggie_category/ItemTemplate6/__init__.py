from ._anvil_designer import ItemTemplate6Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate6(ItemTemplate6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Setze den Rezeptnamen und die Kategorie in den Labels
    self.label_name.text = self.item['Name']
    self.label_description.text = self.item['Description']
    self.label_category.text = self.item['Category']
    self.label_time.text = self.item['PreparationTime']
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """Wird aufgerufen, wenn der Button geklickt wird"""
    recipe_id = self.item['RecipeID']
    # Ruft die Rezeptdetails vom Server ab
    recipe_data = anvil.server.call('get_recipe_details', recipe_id)
    # Öffnet die RecipeCard mit den Rezeptdetails
    open_form('RecipeCard', recipe_data=recipe_data, previous_page="Veggie_category")
