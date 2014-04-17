'''
Created on Apr 6, 2014

@author: hmuriel
'''
import cherrypy
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

class RegisterLogin(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    def register(self):
        # Charger et compléter le template HTML
        return self.env.get_template('inscription.html').render()
    
    def login(self, user_name=None, password=None):
        # Charger et compléter le template HTML
        print(user_name, password)
        if user_name and password:
            # verify login
            raise cherrypy.HTTPRedirect('/compte')
        else:
            return self.env.get_template('login.html').render()
        