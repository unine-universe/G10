DROP TABLE annonce;
CREATE TABLE annonce(id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, publisher TEXT, category INTEGER, faculty TEXT, title TEXT, desc TEXT, price REAL, price_desc TEXT, pub_date TEXT, state TEXT, address, npa INTEGER, city, canton, contact_name, contact_phone);

INSERT INTO annonce VALUES(NULL, 'offer', 'baptistas', 2, 'FSE', 'Mathematica, Le livre', "Le livre de référence sur Mathematica, écrit par l'auteur du programme, Stephen Wolfram. 1500 pages. Comme neuf", 50, 'to_discuss', '2014-04-10T14:08:16.253311', 'online', 'Rue Maladière 23', 2000, 'Neuchâtel', 'Neuchâtel', 'jalex', '0326542345');
INSERT INTO annonce VALUES(NULL, 'offer', 'gauchatl', 3, 'FSE', 'Le Livre de la Jungle', "Livre ancien :1949 Rudyard Kipling Le Second Livre de la Jungle Pour collectionneur ou amateurs. Envoi compris.", 18, '', '2014-03-10T12:08:16.253311', 'archive', '', 1059, 'Peney-le-Jorat', 'Vaud', 'Laetitia', '0327654326');
INSERT INTO annonce VALUES(NULL, 'search', 'gauchatl', 21, 'All', 'Recherche assistant étudiant', "Dr. Ioana Latu, chercheuse dans l'Institut de Psychologie du Travail et des Organisations, recherche un assistant étudiant, taux d’occupation 30-40%, dès maintenant et jusqu’à fin juillet 2014.
Le travail consiste à recruter des participants pour une expérience de psychologie, faire les passations et contribuer à analyser les données pour une expérience dans la réalité virtuelle (UniMail, Neuchâtel). 
Le travail est rémunéré selon le niveau de formation. Le program de travail est flexible. 
Pour en savoir plus, veuillez contacter Ioana Latu à ioana.latu@unine.ch 
Délai de postulation: 15 avril 2014", 25, '', '2014-03-1T12:08:16.253311', 'online', '', 2000, 'Neuchâtel', 'Neuchâtel', '', '0327654326');
INSERT INTO annonce VALUES(NULL, 'search', 'gauchatl', 21, 'All', 'Participer à un focus groupe? Encore des places !', "Bonjour

Dans le cadre d’un enseignement à l’université nous effectuons une recherche exploratoire sur le thème suivant : 
L’automédication et l’influence des sites internet de documentation médicale (tel que Doctissimo) sur la relation patient/ médecin. 

Pour cette étude nous recherchons des personnes bénévoles, intéressées à discuter de ce sujet et de répondre à quelques questions avec nous.

La rencontre aura lieu le 7 avril en début de soirée dans le centre de Neuchâtel. 

Apéritif offert. 

Si vous êtes intéressé, veuillez nous contacter pour plus d’informations.

Tel : 076 489 61 99
Mail : anais.kaiser@unine.ch", 0, 'free', '2014-02-10T12:08:16.253311', 'online', '', 2000, 'Neuchâtel', 'Neuchâtel', 'Laetitia', '0327654326');
INSERT INTO annonce VALUES(NULL, 'search', 'gauchatl', 25, 'All', 'Filmer un vidéo', "Je cherche quelqu'un passionné par filmer des vidéos et qui film bien ,pour filmer ma fête de fiancé pour 2 heures le 04 avril.
Je paye 100 fr
078/696.86.31 /SMS 
candleofnight_m86@yahoo.com", 100, '', '2014-03-20T12:08:16.253311', 'disabled', '', 1007, 'Lausanne', 'Vaud', 'Marie', '078 696 86 31');
INSERT INTO annonce VALUES(NULL, 'offer', 'reratm', 6, 'FSE', 'Je vous donne de soutien pour le cours de Comp. Organisationnel', "Je vous propose des séances de 2 heures pour CHF 20.- de l'heure. ", 20, '', '2014-03-04T20:08:17.253311', 'online', 'Chemin des Pâles 8', 2016, 'Cortaillod', 'Neuchâtel', 'Sophie', '');
INSERT INTO annonce VALUES(NULL, 'offer', 'bettexs', 16, 'FLSH', 'Aide ou assistance en français..', "Bonjour,
Je suis en Master avec bonne maîtrise du Français. Je peux vous accompagner dans la rédaction de vos documents mais aussi pour des perfectionnements en langue française à l'oral et à l'écrit...0779705282", 0, 'to_discuss', '2014-03-01T20:08:17.253311', 'disabled', '', 2000, 'Neuchâtel', 'Neuchâtel', '', '');

DROP TABLE category;
CREATE TABLE category(id INTEGER PRIMARY KEY AUTOINCREMENT, faculty TEXT, name TEXT, parent_cat INTEGER, state TEXT);

INSERT INTO category VALUES(NULL, '', 'Livres', 0, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Livre de cours', 1, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Autres livres', 1, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Roman', 1, 'disabled');
INSERT INTO category VALUES(NULL, '', 'Cours de soutien', 0, 'enabled');
INSERT INTO category VALUES(NULL, 'FSE', 'Comportement organisationnel', 5, 'enabled');
INSERT INTO category VALUES(NULL, 'FSE', 'Histoire de la pensée économique', 5, 'enabled');
INSERT INTO category VALUES(NULL, 'FSE', 'Organisation industrielle', 5, 'enabled');
INSERT INTO category VALUES(NULL, 'FLSH', 'Littérature romande', 5, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Logement', 0, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Colocation', 10, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Appartement', 10, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Chambre individuelle', 10, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Chambre double', 10, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Cours de langue', 0, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Français', 15, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Anglais', 15, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Notes de cours', 0, 'enabled');
INSERT INTO category VALUES(NULL, 'FLSH', 'Civilisation 1500-1700', 18, 'enabled');
INSERT INTO category VALUES(NULL, 'FSE', 'Corporate communication', 18, 'enabled');
INSERT INTO category VALUES(NULL, '', 'Autres', 0, 'enabled');


DROP TABLE picture;
CREATE TABLE picture(a_id INTEGER, pict TEXT, PRIMARY KEY(a_id, pict));
INSERT INTO picture VALUES(2, '/img/annonces/2/010679448-1.jpg');
INSERT INTO picture VALUES(2, '/img/annonces/2/010679452-2.jpg');

DROP TABLE user;
CREATE TABLE user(username TEXT PRIMARY KEY, email TEXT, password TEXT, lastname TEXT, firstname TEXT, age INTEGER, lang TEXT, faculty TEXT, university TEXT, address TEXT, npa INTEGER, city TEXT, canton TEXT, phone TEXT, confirmed TEXT, sms_code TEXT, state TEXT, role TEXT);

INSERT INTO user VALUES('baptistas', 'sofia.baptista@unine.ch', 'baptistas.', 'Baptista', 'Sophia', 23, 'fr', 'FSE', 'Université de Neuchâtel', 'Chemin des Perrières 34', 2072, 'St. Blaise', 'Neuchâtel', '0324567654', 'yes', 'abtr5', 'enabled', 'user');
INSERT INTO user VALUES('gauchatl', 'laetitia.gauchat@unine.ch', 'gauchatl.', 'Gauchat', 'Laetitia', 24, 'fr', 'FSE', 'Université de Neuchâtel', 'Route des Perveuils 2', 2074, 'Marin-Epagnier', 'Neuchâtel', '0320985412', 'yes', '', 'enabled', 'user');
INSERT INTO user VALUES('reratm', 'mathieu.rerat@unine.ch', 'reratm.', 'Rerat', 'Mathieu', 24, 'fr', 'FSE', 'Université de Neuchâtel', 'Route de Beaumont 3', 2068, 'Hauterive', 'Neuchâtel', '0786542387', 'yes', '', 'enabled', 'admin');
INSERT INTO user VALUES('dreyerc', 'camille.dreyer@unine.ch', 'dreyerc.', 'Dreyer', 'Camille', 22, 'fr', 'FSE', 'Université de Neuchâtel', 'Rue de la Main 11', 2000, 'Neuchâtel', 'Neuchâtel', '0786432344', 'yes', 'kiu6d', 'enabled', 'curator');
INSERT INTO user VALUES('jalex', 'jalex@unine.ch', 'jalex.', 'Jaggi', 'Pauline', 23, 'fr', 'FLSH', 'Université de Neuchâtel', 'Rue de la Main 20', 2000, 'Neuchâtel', 'Neuchâtel', '0780962344', 'no', 'kiu6d', 'pending', 'user');
INSERT INTO user VALUES('bettexs', 'sophie.bettexx@unine.ch', 'bettexs.', 'Bettex', 'Sophie', 21, 'en', 'FLSH', 'Université de Neuchâtel', 'Espace Louis-Agassiz 1', 2000, 'Neuchâtel', 'Neuchâtel', '0320967644', 'yes', '', 'disabled', 'user');

DROP TABLE favorite;
CREATE TABLE favorite(user TEXT, a_id INTEGER, date_added TEXT, PRIMARY KEY(user, a_id));
INSERT INTO favorite VALUES('dreyerc', 1, '2014-04-10T16:08:16.253311');
INSERT INTO favorite VALUES('dreyerc', 2, '2014-04-10T16:09:16.253311');
INSERT INTO favorite VALUES('dreyerc', 3, '2014-04-10T16:10:16.253311');
INSERT INTO favorite VALUES('dreyerc', 4, '2014-04-10T16:11:16.253311');
INSERT INTO favorite VALUES('reratm', 4, '2014-04-10T16:20:16.253311');
INSERT INTO favorite VALUES('reratm', 5, '2014-04-10T16:21:16.253311');