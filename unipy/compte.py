'''
Created on Apr 6, 2014

@author: hmuriel
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB

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
        
    def annoncesEnLigne(self, user=None):
        if user:
            db = openDB()
            cursor = db.cursor()
            # Annonces
            cursor.execute("SELECT * FROM annonce WHERE publisher='{0}'".format(user))
            annonces_user = cursor.fetchall() # prendre tous les annonces
            # Pictures
            pictures = {}
            for a in annonces_user:
                cursor.execute("SELECT pict FROM picture WHERE a_id='{0}'".format(a[0]))
                pictures[a[0]] = cursor.fetchall()
            cursor.close()
            db.close()
            if annonces_user:
                # Charger et compléter le template HTML
                return self.env.get_template('mesAnnoncesEnLigne.html').render(annonces = annonces_user, pics = pictures)
            else:
                return "<h1>Erreur, utilisateur inexistant ou vous n'avez pas de droits.</h1>"
        else:
            return "<h1>Indiquez l'utilisateur ?user=username</h1>"
        
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