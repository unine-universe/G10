'''
Created on Apr 6, 2014

@author: hmuriel
'''
import cherrypy
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB

class Rubrique(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    def rubriques(self):
        # Charger et compléter le template HTML
        return self.env.get_template('adminRubriques.html').render()