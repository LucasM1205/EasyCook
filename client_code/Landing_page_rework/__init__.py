from ._anvil_designer import Landing_page_reworkTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Landing_page_rework(Landing_page_reworkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Event-Handler für den Button zuweisen
    #get_started_button = self.get_element_by_id('get-started')
    #get_started_button.set_event_handler('click', self.button_click)

  def form_show(self, **event_args):
    """This method is called when the form is shown on the screen."""
    # Call the JavaScript function to assign the event handler
    self.call_js('assignButtonEventHandler')



  def get_started_click(self, **event_args):
    """This method is called when the 'Get Started' button is clicked"""
    open_form('Main_page')
