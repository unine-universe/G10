'''
Created on Apr 6, 2014

@author: hmuriel
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB

class GestionUtilisateur(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    def adminUsers(self):
        # Charger et compléter le template HTML
        return self.env.get_template('GestionUserAdmin.html').render()
    
    def adminUser(self, user):
        # Charger et compléter le template HTML
        return '<h1>User:' + user + '</h1>' + self.env.get_template('monCompteAdmin.html').render()