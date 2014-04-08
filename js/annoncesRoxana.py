'''
Created on Apr 7, 2014

@author: Roxana
'''
import cherrypy

class Annonces(annonce):
    header= '<html><head><title>UniVerse: Student Exchange!</title></head>'
    footer= '</html>'
    
    @cherrypy.expose()
        def annonces(self):
        # Charger et compléter le template HTML
        return self.env.get_template('annonces.html').render()
        content= '<body><h1>Annonces Moderateur</h1><a hred="/annonces">Voir les annonces</a></body>'
        return self.header + content + self.footer
    
 
