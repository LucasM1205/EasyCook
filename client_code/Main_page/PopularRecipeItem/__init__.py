from ._anvil_designer import PopularRecipeItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class PopularRecipeItem(PopularRecipeItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #Setze das Bild und andere Elemente
    self.image_1.source = self.item['RecipePicture']
    #self.label_name.text = self.item['Name']

  def image_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    recipe_id = self.item['RecipeID']
    recipe_data = anvil.server.call('get_recipe_details', recipe_id)
    #open_form('RecipeCard', recipe_data={'recipe': self.item, 'details': recipe_details}, previous_page="Main_page")
    open_form('RecipeCard', recipe_data=recipe_data, previous_page="Main_page")