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
    self.search_results_panel.items = []  # Initial leere Suchergebnisse
    while not anvil.users.login_with_form(allow_cancel=True):
      pass
    # Beliebte Rezepte laden und anzeigen
    self.load_popular_recipes()
    #self.load_user_favorites()
    self.load_favorite_recipes()

  def load_popular_recipes(self):
    # Abrufen der beliebten Rezepte vom Server
    popular_recipes = anvil.server.call('get_popular_recipes')
    self.popular_recipes_panel.items = popular_recipes

  def load_favorite_recipes(self):
    favorite_recipes = anvil.server.call('get_favorite_recipes')
    self.favorites_repeating_panel.items = favorite_recipes

  
  def open_recipe(self, recipe):
    # Abrufen der Rezeptdetails und Öffnen der RecipeCard
    recipe_details = anvil.server.call('get_recipe_details', recipe['RecipeID'])
    open_form('RecipeCard', recipe=recipe_details, previous_page="Main_page")
  
  def search_box_change(self, **event_args):
    """This method is called when the user types in the search box"""
    keyword = self.search_box.text
    if keyword:
      results = anvil.server.call('search_recipes', keyword)
      self.search_results_panel.items = results
    else:
      self.search_results_panel.items = [] # Keine Suchergebnisse, wenn kein Keyword eingegeben

  def elevated_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Ingredient_Selection_Page_copy')

  def elevated_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_page.Veggie_category')

  def elevated_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_page.Meat_category')

  def elevated_button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_page.Sweet_category')

  def search_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    selected_recipe = self.search_results_panel.selected_item
    if selected_recipe:
      open_form('RecipeCard', recipe=selected_recipe)
