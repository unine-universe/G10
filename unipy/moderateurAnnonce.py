'''
Created on Apr 6, 2014

@author: hmuriel
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

class ModerateurAnnonce(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    def annonces(self):
        # Charger et compléter le template HTML
        return self.env.get_template('annoncesModerateur.html').render()
    