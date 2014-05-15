'''
Created on Apr 6, 2014

@author: hmuriel
'''
import cherrypy
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB

class RegisterLogin(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    def inscription(self):
        # Charger et compléter le template HTML
        return self.env.get_template('creationCompte.html').render()
    
    def confirmerSMS(self):
        # Charger et compléter le template HTML
        return self.env.get_template('confirmationCompteSMS.html').render()
    
    def confirmerEmail(self):
        # Charger et compléter le template HTML
        return self.env.get_template('confirmationCompteEmail.html').render()
    
    def login(self, user_name=None, password=None):
        # Charger et compléter le template HTML
        if user_name and password:
            # verify login
            print(cherrypy.url())
            # after login
            cherrypy.session[SESSION_KEY] = cherrypy.request.login = user_name
            raise cherrypy.HTTPRedirect("/compte")
        else:
            return self.env.get_template('login.html').render()

    def logout(self):
        cherrypy.session[SESSION_KEY] = None
        cherrypy.request.login = None
        raise cherrypy.HTTPRedirect("/")
    

SESSION_KEY = 'universe_session'
def getUsername():
    return cherrypy.session.get(SESSION_KEY)
    
def check_auth(*args, **kwargs):
    conditions = cherrypy.request.config.get('auth.require', None)
    if conditions is not None:
        username = cherrypy.session.get(SESSION_KEY)
        if username:
            # garder le nom d'utilisateur
            cherrypy.request.login = username
            for condition in conditions:
                if not condition():
                    raise cherrypy.HTTPRedirect("/login")
        else:
            raise cherrypy.HTTPRedirect("/login")
cherrypy.tools.auth = cherrypy.Tool('before_handler', check_auth)

def member_of(groupname):
    def check():
        is_member = False
        db = openDB()
        c = db.cursor()
        # Vérifier dans la base de données si l'utilisateur appartient à groupname
        
        c.close()
        db.close()
        
        return True
    return check

def require(*conditions):
    def decorate(f):
        if not hasattr(f, '_cp_config'):
            f._cp_config = dict()
        if 'auth.require' not in f._cp_config:
            f._cp_config['auth.require'] = []
        f._cp_config['auth.require'].extend(conditions)
        return f
    return decorate

def any_of(*conditions):
    """Returns True if any of the conditions match"""
    def check():
        for c in conditions:
            if c():
                return True
        return False
    return check