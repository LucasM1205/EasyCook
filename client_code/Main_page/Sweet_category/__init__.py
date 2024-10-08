from ._anvil_designer import Sweet_categoryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Sweet_category(Sweet_categoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.recipes.search(Category="Dessert")
    self.repeating_panel_1.set_event_handler('x-show-ingredients-alert', self.show_ingredients_alert)
    self.repeating_panel_2.items = app_tables.recipes.search(Category="Dessert")

    # Any code you write here will run before the form opens.
  def show_ingredients_alert(self, recipe_id, **event_args):
    ingredients = anvil.server.call('get_ingredients_for_recipe', recipe_id)
    ingredient_list = "\n".join([f"{ingredient['quantity']} {ingredient['unit']} {ingredient['name']}" for ingredient in ingredients])
    alert(content=ingredient_list, title="Ingredients", large=True)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Main_page")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_page')
