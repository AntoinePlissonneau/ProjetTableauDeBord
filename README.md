# Projet Tableau De Bord
Projet M1 SID Tableau de bord (Amira Ayadi, Antoine Plissonneau)

###Outils utilisés

* Github: Pour travailler sur exactement les mêmes fichiers 
* Python:
 * __requests, urlib__ : gère les différentes requêtes http, utilisé pour acceder aux differentes pages web (résultats recherche et pdf)
 * **PDFminer**: parser de pdf 
 * __BeautifulSoup__: parser de page web
 * __json__: permets de créer des fichiers JSON
* Pile ELK?:
 * __Logstash__
 * __ElasticSearch__
 * __Kibana__
* MongoDB?
* SQLServer?

###Ressources utilisées

* IOPScience
* Web Of Science


###Schéma
![sart1](Images/SchemaExplicatif.png)

###Collecte des pdf
#####1/Requetes http via python 
#####2/Gestion de l'authentification UPS
* Pas une authentification simple mais une redirection

#####3/Extraction métadonnées et collecte des liens pdf
#####4/Téléchargement des pdfs liés

###Extraction des données
#####1/Texte
* pdfminer

#####2/Images
* pyPDF2

XOBJECT

#####3/Figures
* pdffigures

Ce que fait le programme:
 
Outil pas encore assez développé

###Mise en relation figure/texte
#####1/Avec le numéro de la figure
#####2/Avec une analyse de la similarité lexicale
* rake
* KEA
* Stemming
* tf-idf
* Vector
* Cosine

###Base de donnée mongoDB
#####Intro: choix d'une base noSQL
#####1/Création de la base et injection des données

###Tableau de bord
I/Figure/Référence/Légende
* affichage
* précision:Références directes bien retrouvées par le ranking
* rappel?: Références ajoutées par le ranking
II/Matrice de relation entre documents (tf-idf)
* faire ressortir les docs liés
* graph/network de relation

