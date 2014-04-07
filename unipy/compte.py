'''
Created on Apr 6, 2014

@author: hmuriel
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

class Compte(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    def index(self):
        # Charger et compléter le template HTML
        return self.env.get_template('monCompte.html').render()
    
    def annonces(self):
        # Charger et compléter le template HTML
        return self.env.get_template('mesAnnonces.html').render()
    
    def annoncesEnLigne(self):
        # Charger et compléter le template HTML
        return self.env.get_template('mesAnnoncesEnLigne.html').render()
    
    def annoncesArchives(self):
        # Charger et compléter le template HTML
        return self.env.get_template('mesAnnoncesArchives.html').render()
    
    def favoris(self):
        # Charger et compléter le template HTML
        return self.env.get_template('mesFavoris.html').render()
    
    def favorisAnnonces(self):
        # Charger et compléter le template HTML
        return self.env.get_template('mesFavorisAnnonces.html').render()
    
    def favorisRecherche(self):
        # Charger et compléter le template HTML
        return self.env.get_template('mesFavorisRecherches.html').render()
    
    def changerMotDePasse(self):
        # Charger et compléter le template HTML
        return self.env.get_template('monCompteChangePWD.html').render()