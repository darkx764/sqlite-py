import os
from classes.cli_prompter import menu

class databases:
    """ Databases Manager ."""
    def __init__(self):
        # try to check if database folder exists or not
        pass

    def list(self, path):
        """ list all databases available in databases folder. """
        try:
            return os.listdir(path)
        except Exception as e:
            print(f"Exception in databases.py : {e}")
    
    def show(self):
        """ prompt menu with all tables available. """
        return menu.select("Choose your DB: ", self.list('databases'))