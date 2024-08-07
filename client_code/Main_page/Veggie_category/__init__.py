from ._anvil_designer import Veggie_categoryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Veggie_category(Veggie_categoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.recipes.search(Category="Veggie")
    # Any code you write here will run before the form opens.

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Main_page')

  def get_ingredients_for_recipe(self, recipe_id):
        recipe_ingredients = app_tables.recipe_ingredients.search(RecipeID=recipe_id)
        ingredients = []
        for item in recipe_ingredients:
            ingredient = app_tables.ingredients.get(IngredientID=item['IngredientID'])
            ingredients.append({
                'name': ingredient['Name'],
                'quantity': item['Quantity']
            })
        return ingredients

  def show_recipe_detail(self, recipe):
        recipe_detail_form = RecipeDetailForm()
        recipe_detail_form.label_recipe_name.text = recipe['Name']
        recipe_detail_form.repeating_panel_ingredients.items = self.get_ingredients_for_recipe(recipe['RecipeID'])
        open_form(recipe_detail_form)

  def repeating_panel_1_item_click(self, **event_args):
        selected_recipe = self.repeating_panel_1.get_components()[event_args['item_index']]
        self.show_recipe_detail(selected_recipe)

