# Projet 10 - Créez une API sécurisée RESTful en utilisant Django REST - OpenClassrooms

<img src="img/logoSoftDesk.png" width="200" height="250">

Cet application permet de remonter et suivre des problèmes techniques (issue tracking system).

## Mise en place du projet: 

#### I) Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.

###### - Récupération du projet

    $ git clone https://github.com/Appryll/Projet-10-Creez-une-API-securisee-RESTful-en-utilisant-Django-REST.git

    Se déplacer dans le repertoire du projet :

    $ cd Projet-10-Creez-une-API-securisee-RESTful-en-utilisant-Django-REST-master

###### -Créer et activer l'environnement virtuel 
    $ python -m venv env 
    $ ~env\scripts\activate
    
###### - Installer les paquets requis
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    Se déplacer vers le repertoire config: 
    $ cd config
    $ python manage.py runserver

    Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut. Si le port n'est pas 
    disponible :
    $ python manage.py runserver <your_port>

###### - Naviguer sur le site
    Ouvrir un navigateur, et aller à l'adresse du site. ex : http://127.0.0.1:8000/

###### - Quitter l'envirement virtuel
    deactivate

-----
#### II) MacOS, Linux :
Dans le terminal, naviguer vers le dossier souhaité.

###### - Récupération du projet
     $ git clone https://github.com/Appryll/Projet-10-Creez-une-API-securisee-RESTful-en-utilisant-Django-REST.git

    Se déplacer dans le repertoire du projet :
    $ cd Projet-10-Creez-une-API-securisee-RESTful-en-utilisant-Django-REST-master

###### -Créer et activer l'environnement virtuel
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### - Installer les paquets requis
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    Se déplacer vers le repertoire config: 
    $ cd config
    $ python3 manage.py runserver

    Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut. Si le port n'est pas 
    disponible :
    $ python3 manage.py runserver <your_port>

###### - Naviguer sur le site
    Ouvrir un navigateur, et aller à l'adresse du site. ex : http://127.0.0.1:8000/

###### - Quitter l'envirement virtuel
    deactivate

------------------------------------------------------------------------------------------------------------------------

