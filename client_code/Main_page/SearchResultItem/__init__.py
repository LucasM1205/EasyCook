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
    # Any code you write here will run before the form opens.
