from ._anvil_designer import RecipeSuggestionFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RecipeSuggestionForm(RecipeSuggestionFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_name.text
    description = self.text_area_description.text
    duration = self.text_box_duration.text
    ingredients = self.text_area_ingredients.text
    preparation_steps = self.text_area_preparation_steps.text
    # Validate the inputs
    if not name or not description or not duration or not ingredients or not preparation_steps:
      alert("Please fill in all fields.")
      return
    # Send the recipe data to the server
    result = anvil.server.call('send_recipe_suggestion', name, description, duration, ingredients, preparation_steps)
    if result == "success":
      alert("Thank you for your suggestion! We will review it.")
      self.reset_form()
    else:
      alert(f"There was a problem sending your suggestion: {result}")

  def button_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.reset_form()
    open_form('Main_page')

  def reset_form(self):
    self.text_box_name.text = ""
    self.text_area_description.text = ""
    self.text_box_duration.text = ""
    self.text_area_ingredients.text = ""
    self.text_area_preparation_steps.text = ""