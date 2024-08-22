from ._anvil_designer import CommentTemplateTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CommentTemplate(CommentTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Binden Sie die Datenfelder
    self.label_username_display.text = self.item['User']['email']
    self.label_comment.text = self.item['CommentText']
    self.label_timestamp.text = self.item['Timestamp'].strftime("%d %b %Y, %H:%M")
    # Any code you write here will run before the form opens.
