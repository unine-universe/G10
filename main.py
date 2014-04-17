'''
Created on Apr 6, 2014

@author: hmuriel
'''
import cherrypy
import os
from unipy.annonces import Annonces
from unipy.compte import Compte
from unipy.creerAnnonce import CreerAnnonce
from unipy.registerLogin import RegisterLogin
from unipy.moderateurAnnonce import ModerateurAnnonce
from unipy.gestionUtilisateur import GestionUtilisateur
from unipy.rubriques import Rubrique

# Paramètres pour cherrypy, pas besoin de les modifier.
cherrypy.config.update({
    # 'environment': 'production',
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 8080,
    'log.error_file': 'site.log',
    'log.screen': True,
    'tools.sessions.on': True
})

# Racine de l'application
root_path = os.path.dirname(__file__)
# Controlleurs
annonces = Annonces()
compte = Compte()
creerannonce = CreerAnnonce()
register_login = RegisterLogin()
moderateurAnnonces = ModerateurAnnonce()
gestion_user = GestionUtilisateur()
rubrique = Rubrique()

# Gestionnaire des chemins d'accès (p. ex. /annonces/new)
d = cherrypy.dispatch.RoutesDispatcher()
# d.connect('NOM POUR LE CHEMIN',    'CHEMIN depuis la racine',    'OBJECT'                , 'METHODE')
d.connect('accueil'                , '/'                            , controller=annonces, action='annonces')
d.connect('annonce'                , '/annonce'                     , controller=annonces, action='annonce')
d.connect('mon-compte'             , '/compte'                      , controller=compte, action='index')
d.connect('mes-annonces'           , '/compte/annonces'             , controller=compte, action='annonces')
d.connect('mes-annonces-enligne'   , '/compte/annonces/enligne'       , controller=compte, action='annoncesEnLigne')
d.connect('mes-annonces-archives'  , '/compte/annonces/archives'    , controller=compte, action='annoncesArchives')
d.connect('mes-favoris'            , '/compte/favoris'              , controller=compte, action='favoris')
d.connect('mes-favoris-annonces'   , '/compte/favoris/annonces'     , controller=compte, action='favorisAnnonces')
d.connect('mes-favoris-recherche'  , '/compte/favoris/recherche'    , controller=compte, action='favorisRecherche')
d.connect('creer-annonce'          , '/creer-annonce'               , controller=creerannonce, action='creer')
d.connect('enregistrer-annonce'    , '/creer/sauvegarder'           , controller=creerannonce, action='save')
d.connect('changer-motdepasse'     , '/compte/change-motdepasse'    , controller=compte, action='changerMotDePasse')
d.connect('mon-profil'             , '/compte/profil'               , controller=compte, action='profile')
d.connect('login'                  , '/login'                       , controller=register_login, action='login')
d.connect('moderateur-admin'       , '/admin'                       , controller=moderateurAnnonces, action='annonces_accueil')
d.connect('moderateur-annonces'    , '/admin/annonces'              , controller=moderateurAnnonces, action='annonces')
d.connect('moderateur-annonce'     , '/admin/annonce'               , controller=moderateurAnnonces, action='annonce')
d.connect('moderateur-a-effacer'   , '/admin/annonce/delete'        , controller=moderateurAnnonces, action='remove')
d.connect('admin-users'            , '/admin/users'                 , controller=gestion_user, action='adminUsers')
d.connect('admin-user'             , '/admin/user'                  , controller=gestion_user, action='adminUser')
d.connect('rubriques'              , '/admin/rubriques'             , controller=rubrique, action='rubriques')
d.connect('rubriques'              , '/admin/rubriques'             , controller=rubrique, action='rubriques')
d.connect('inscription'            , '/inscription'                 , controller=register_login, action='inscription')
d.connect('inscrip-conf-sms'       , '/inscription/confirmer-sms'   , controller=register_login, action='confirmerSMS')
d.connect('inscrip-conf-email'     , '/inscription/confirmer-email' , controller=register_login, action='confirmerEmail')

# Configuration pour l'application
conf = {
        # Gestionnaire des chemins d'accès et la racine des dossiers.
        '/' : {'request.dispatch' : d, 'tools.staticdir.root':root_path},
        # Publication du dossier des images 
        '/img':{'tools.staticdir.on' : True, 'tools.staticdir.dir' :'img'},
        # Publication du dossier CSS
        '/css':{'tools.staticdir.on' : True, 'tools.staticdir.dir' :'css'},
        # Publication du dossier JS
        '/js':{'tools.staticdir.on' : True, 'tools.staticdir.dir' :'js'}
        }
# Démarrage du serveur cherrypy
cherrypy.quickstart(annonces, '/', conf)