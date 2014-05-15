'''
Created on Apr 6, 2014

@author: hmuriel
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB
from unipy.registerLogin import require, member_of, any_of

class ModerateurAnnonce(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    @require(any_of(member_of('admin'), member_of('curator')))
    def annonces_accueil(self):
        # Charger et compléter le template HTML
        return self.env.get_template('adminGestion.html').render()
    
    def annonces(self):
        # Charger et compléter le template HTML
        return self.env.get_template('adminAnnonces.html').render()
        
    def annonce(self, a_id):
        db = openDB()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM annonce WHERE id='{0}'".format(a_id))
        annonce = cursor.fetchone() # prendre une ligne. fetchall() égal à tous les lignes.
        
        cursor.close()
        db.close()
        if annonce:
            # Charger et compléter le template HTML
            return self.env.get_template('annoncesModerateur.html').render(a_id = annonce[0], prix = annonce[7], desc = annonce[6])
        else:
            return '<h1>Erreur, annonce inexistante</h1>'
    
    def remove(self, a_id):
        db = openDB()
        cursor = db.cursor()
        cursor.execute("DELETE FROM annonce WHERE id='{0}'".format(a_id))
        # Transmettre le SQL de type INSERT, UPDATE, DELETE
        db.commit()
        cursor.close()
        db.close()
        
        return '<h1>Annonce {0} effacée</h1><p><a href="/admin/annonces">Retour</a></p>'.format(a_id)
        
    def bloquer(self, a_id):
        db = openDB()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM annonce WHERE id='{0}'".format(a_id))
        
        
        if bloquer:
            # Charger et compléter le template HTML
            return  # Email utilisateurs et modérateur. Besoin de faire le lien avec la base de données Users.
            #return self.env.get_template('annoncesModerateur.html').render(a_id = annonce[0], prix = annonce[7], desc = annonce[6])
        else:
            return '<h1>Erreur, annonce bloquée</h1>'
        
        db.commit()
        cursor.close()
        db.close()
    
    def modifier(self, a_id):
         db = openDB()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM annonce WHERE id='{0}'".format(a_id))
        
        
        if modifier:
            
            # Charger et compléter le template HTML
            
            return  # Email utilisateurs et modérateur. Besoin de faire le lien avec la base de données Users. 
                    # 
            
        db.commit()
        cursor.close()
        db.close()
        
        
