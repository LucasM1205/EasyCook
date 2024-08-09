from ._anvil_designer import IngredientItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class IngredientItem(IngredientItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Set the data bindings
    self.check_box_1.checked = self.item['selected']
    self.label_1.text = self.item['ingredient']

  def check_box_1_change(self, **event_args):
    """This method is called when the check box is changed"""
    self.item['selected'] = self.check_box_1.checked
    # Debugging-Ausgabe, um zu sehen, wann sich der Wert ändert
    print(f"{self.item['ingredient']} selected: {self.item['selected']}")
    #if hasattr(self.parent, 'update_selection'):
      #self.parent.update_selection()
    # Any code you write here will run before the form opens.
