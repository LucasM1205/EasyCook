from ._anvil_designer import RecipeCardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RecipeCard(RecipeCardTemplate):
  def __init__(self, recipe_data, previous_page, selected_ingredients=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Entpacken des Row-Objekts und der Details
    self.recipe = recipe_data['recipe']
    details = recipe_data['details']
    self.previous_page = previous_page
    self.selected_ingredients = selected_ingredients
    
    # Setze die Daten für das ausgewählte Rezept
    self.image_1.source = details['RecipePicture']
    self.label_name.text = details['Name']
    self.label_ingredients.text = self.format_ingredients(details['Ingredients'])
    self.label_preparation.text = details['PreparationSteps']
    self.label_prep_time.text = f"Preparation Time: {self.recipe['PreparationTime']} Minutes"

    #Lade die Anzahl der Favoriten
    self.label_favorites_count.text = f"{self.recipe['FavoritesCount']} People's favourite"
    
    # Lade die Kommentare
    self.load_comments()
    
    # Überprüfe, ob das Rezept bereits ein Favorit ist
    self.update_favorite_status()

    # Setze den Schwierigkeitsgrad
    self.set_difficulty_label()

  def set_difficulty_label(self):
    difficulty = self.recipe['Difficulty'].lower() 
        
    if difficulty == 'easy':
      difficulty_text = "Easy"
      difficulty_color = '#92d050'
    elif difficulty == 'medium':
      difficulty_text = "Medium"
      difficulty_color = '#ffa500'  # Orange als Alternative zu Gelb
    elif difficulty == 'hard':
      difficulty_text = "Hard"
      difficulty_color = '#ff0000'  # Rot für "Hard"
    else:
      difficulty_text = "Unknown"
      difficulty_color = '#000000'  # Standardfarbe für unbekannte Schwierigkeitsgrade

    # Setze den Text und die Farbe
    self.label_difficulty.text = f"{difficulty_text}"
    self.label_difficulty.foreground = difficulty_color

  def load_comments(self):
    comments = anvil.server.call('get_comments_for_recipe', self.recipe['RecipeID'])
    # Debugging: Kommentare überprüfen
    print("Geladene Kommentare:", comments)
    for comment in comments:
        if 'username_display' not in comment or comment['username_display'] == 'Unbekannt':
            comment['username_display'] = 'Unknown User'  # Setze einen Standardwert
    self.repeating_panel_comments.items = comments

  def format_ingredients(self, ingredients):
    return "\n".join([f"{ing['quantity']} {ing['unit']} {ing['name']}" for ing in ingredients])
  
  def back_button_click(self, **event_args):
    """Zurück zur vorherigen Seite"""
    if self.previous_page == "Main_page":
        open_form('Main_page')
    elif self.previous_page == "RecipeResultsPage":
        open_form('RecipeResultsPage', selected_ingredients=self.selected_ingredients)
    elif self.previous_page == "Meat_category":
        open_form('Main_page.Meat_category')
    elif self.previous_page == "Sweet_category":
        open_form('Main_page.Sweet_category')
    elif self.previous_page == "Veggie_category":
        open_form('Main_page.Veggie_category')

  def update_favorite_status(self):
    # Überprüfen, ob das Rezept bereits als Favorit markiert ist
    is_favorite = anvil.server.call('is_favorite', self.recipe)
    self.check_box_favorite.checked = is_favorite

  def check_box_favorite_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.check_box_favorite.checked:
        print("Adding to favorites")
        anvil.server.call('add_to_favorites', self.recipe)
    else:
        print("Removing from favorites")
        anvil.server.call('remove_from_favorites', self.recipe)

    # Favoriten-Zähler nach der Aktualisierung neu laden
    self.recipe = anvil.server.call('get_recipe_details', self.recipe['RecipeID'])['recipe']
    self.label_favorites_count.text = f"{self.recipe['FavoritesCount']} People's favourite"

  def button_1_click(self, **event_args):
    """Wird aufgerufen, wenn der Button geklickt wird, um einen Kommentar hinzuzufügen"""
    comment_text = self.text_area_1.text
    if comment_text:
      anvil.server.call('add_comment', self.recipe['RecipeID'], comment_text)
      self.text_area_1.text = ''  # Clear the text box
      self.load_comments()  # Reload the comments
    else:
      alert("Comment cannot be empty.")


