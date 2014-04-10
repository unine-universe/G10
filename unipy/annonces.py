'''
Created on Apr 6, 2014

@author: hmuriel
'''
import cherrypy
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB

class Annonces(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
        
    def annonces(self):
        # Charger et compléter le template HTML
        return self.env.get_template('afficherAnnonces.html').render()
    
    def annonce(self, a_id):
        db = openDB()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM annonce WHERE id='{0}'".format(a_id))
        annonce = cursor.fetchone() # prendre une ligne. fetchall() égal à tous les lignes.
        
        cursor.close()
        db.close()
        cherrypy.log.error(str(type(annonce)))
        if annonce:
            # Charger et compléter le template HTML
            return self.env.get_template('afficherAnnonce.html').render(prix = annonce[6], desc = annonce[5])
        else:
            return '<h1>Erreur, annonce inexistante</h1>'