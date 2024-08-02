import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
# für das Hinzufügen von Daten zu den Tabellen

import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def add_ingredient(name, categorie):
    app_tables.ingredients.add_row(Name=name, Category=category)

@anvil.server.callable
def add_recipe(name, description, categorie, preparation_time):
    app_tables.recipes.add_row(Name=name, Description=description, Category=category, PreparationTime=preparation_time)

@anvil.server.callable
def add_recepie_ingredient(recepie_id, ingredient_id, cuantity):
    recipe = app_tables.recipes.get(ID=recipe_id)
    ingredient = app_tables.ingredients.get(ID=ingredient_id)
    app_tables.recepie_ingredients.add_row(RecepieID=recepie, IngredientID=ingredient, Cuantity=cuantity)
