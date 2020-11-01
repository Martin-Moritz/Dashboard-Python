# Projet Python - ESIEE Paris : Écart salarial femmes-hommes

Projet python dont l'objectif est de créer un dashboard interactif permettant de visualiser et d'analyser de manière pertinente un jeu de données.

## 1 - User Guide

### **Installation**

*Installer python au préalable sur la machine utilisée*

##### Ouvrir le terminal de commande

> *Windows* et *Linux* : chercher en tapant '*terminal*' dans la barre de recherche.

##### Se placer dans le dossier du projet

> Utiliser la commande `cd <chemin du répertoire>`
<br/>par exemple : 'cd Desktop/projet-python-e4-dashboard'

##### Installer tous les modules/packages nécessaires de python

Exécuter la commande `pip install -r requirements.txt`

ou `python3 -m pip install -r requirements.txt` dans le terminal.

### **Utilisation**

*Après avoir téléchargé le dossier du projet :*

- Ouvrir le terminal de commande

- Se placer dans le dossier du projet

- Exécuter la commande `python3 main.py` pour démarrer l'application

- Attendre quelques instants le chargement de l'application

Si tout se passe bien :

&nbsp;
![CMD](rapport/cmd.PNG)
&nbsp;

- Ouvrir son navigateur internet et afficher le dashboard en *localhost* (entrez l'adresse suivante dans votre navigateur : http://127.0.0.1:5000/)

- Appuyer CTLR+C dans le terminal pour quitter l'application

## 2 - Developer Guide

#### Architecture du projet

Le projet est constitué de :

- 4 dossiers :

  - **pycache** : contient une version compressée des modules python afin d'accélérer leur chargement.
  - **app** : contient l'ensemble du code de l'application.
  - **data** : contient les fichiers .csv des données utilisées pour ce projet.
  - **rapport** : contient les images affichées dans le rapport d'analyse ci-dessous.

* 3 fichiers :

  * **main.py** : fichier python permettant de lancer l'application.
  * **requirements.txt** : liste des modules/packages utilisés dans cette application.
  * **README.md**

#### Architecture du dossier **app**

Le dossier app est constitué d'un dossier *pycache* et de 7 fichiers python :

- **init.py** : permet de créer l'application *flask*.
- **callbacks.py** : contient les fonctions qui permettent d'obtenir des graphiques interactifs.
- **dash.py** : permet de convertir l'application *flask* en une application *Dash*, permettant ainsi la création du dashboard.
- **data.py** : contient le code permettant de trier les jeux de données contenus dans le dossier .data
- **figures.py** : contient les fonctions qui créent les différentes figures et graphiques du dashboard.
- **layout.py** : contient le code permettant de disposer les différents compososants et figures sur la page, déterminant ainsi l'aspect du dashboard.
- **navbar.py** : contient le code déterminant l'aspect de la barre de navigation située en haut de la page.

#### Fonctions des différents fichiers

- **callbacks.py** :
  - *update_carte(selected_countries, selected_salarial)*
  > Met à jour la carte choroplèthe en fonction des pays choisis dans le menu déroulant, ainsi qu'en fonction du type d'emploi sélectionné.

  - *update_histogramme(selected_countries, selected_salarial, selected_year)*
  > Met à jour l'histogramme en fonction des pays et du type d'emploi choisis, ainsi que de l'année sélectionnée sur le slider situé en dessous.

  - *update_diagramme(selected_countries, selected_salarial, selected_year)*
  > Met à jour le diagramme en barres en fonction des pays et du type d'emploi choisis, ainsi que de l'année sélectionnée sur le slider situé en dessous.

  - *update_slider(selected_countries, selected_salarial)*
  > Met à jour le slider en fonction des pays et du type d'emploi choisis pour pouvoir sélectionner des années où des données sont présentes.

  - *update_dropdown(selected_salarial)*
  > Permet d'activer ou désactiver le menu déroulant en fonction du type d'emploi sélectionné.

  - *update_graphe(selected_countries, selected_salarial)*
  > Met à jour le premier graphique en fonction des pays choisis dans le menu déroulant, ainsi qu'en fonction du type d'emploi sélectionné.

- **figures.py** :
  - *create_carte(df,focus='world')*
  > Crée la carte choroplèthe avec la dataframe et le focus donnés en paramètres.

  - *create_histogramme(df, year)*
  > Crée l'histogramme avec la dataframe et l'année donnés en paramètres.

  - *create_diagramme(df, year)*
  > Crée le diagramme en barres avec la dataframe et l'année donnés en paramètres.

  - *create_graphe(df)*
  > Crée le premier graphique avec la dataframe donnée en paramètre.

## 3 - Rapport d'analyse

#### Définition de l'Écart salarial femmes-hommes :
L’écart salarial entre les femmes et les hommes est défini comme la différence entre le salaire médian des hommes et des femmes rapportée au salaire médian des hommes. Les données se rapportent d’une part aux salariés à plein temps et de l’autre aux non-salariés.

## Dataset

Data utilisée pour l'analyse : https://data.oecd.org/fr/earnwage/ecart-salarial-femmes-hommes.htm

Data secondaire (utilisée pour avoir les noms des pays et des continents en français) :

  - https://sql.sh/ressources/sql-pays/sql-pays.csv
  - https://pkgstore.datahub.io/JohnSnowLabs/country-and-continent-codes-list/country-and-continent-codes-list-csv_csv/data/b7876b7f496677669644f3d1069d3121/country-and-continent-codes-list-csv_csv.csv
