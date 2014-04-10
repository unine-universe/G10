'''
Created on Apr 6, 2014

@author: hmuriel
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB

class ModerateurAnnonce(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    def annonces(self):
        # Charger et compléter le template HTML
        return self.env.get_template('annoncesModerateur.html').render()
    
    def remove(self, a_id):
        db = openDB()
        cursor = db.cursor()
        cursor.execute("DELETE FROM annonce WHERE id='{0}'".format(a_id))
        # Transmettre le SQL de type INSERT, UPDATE, DELETE
        db.commit()
        cursor.close()
        db.close()
        
        return '<h1>Annonce {0} effacée</h1><p><a href="/admin/annonces">Retour</a></p>'.format(a_id)
        