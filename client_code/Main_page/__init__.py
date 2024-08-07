from ._anvil_designer import Main_pageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class Main_page(Main_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    while not anvil.users.login_with_form(allow_cancel=True):
      pass

  def elevated_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Ingredient_Selection_Page')

  def elevated_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_page.Veggie_category')

  def elevated_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_page.Meat_category')

  def elevated_button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_page')