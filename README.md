# Projet Python 
#### Effectué par @Foufou-exe(Thibaut Maurras) et @thorbeorn(Dylan Llodra)
Rendu prevu le 04/12/2022

### Mission :

- Lire le csv
- Extraire les données
- Parsing
    - Nettoyages
        - Supprimer toutes les lignes avec au moins une cellule vide
        - Supression des colonnes A,D,E,F,G
- Fichier de sortie: clean.csv
    - Regroupement par organisation

Fichier Final : **clean.csv** \
**Tri par type(alphabetique) et consommation annuelle total(decroissant)**

*Liens* :

[![Google](https://img.shields.io/static/v1?label=%20&message=Exercice&color=red&style=for-the-badge&logoColor=FDFEFE&logo=googledrive)](https://docs.google.com/spreadsheets/d/1ZFNds1t05Xn_gfj2G8lZhgpmwV7xU1qP4u00XShbLtg/edit?usp=sharing) [![Google](https://img.shields.io/static/v1?label=%20&message=Projet&color=red&style=for-the-badge&logoColor=FDFEFE&logo=googledrive)](https://docs.google.com/spreadsheets/d/1BnthgpieVAsnWahYs3PI1_dhVF5dIJfEtB5Z1pUi018/edit?usp=sharing) 

### Ajout Bonus :
**Premier ajout** : *Option de lancement*

On peut choisir un fichier qu'on veut et le definir grace à des options entrer et sortie de le lancement du script.

**Exemple** : main.py ***-s fichier.csv -o fichier-clean.csv*** 

*Avec l'option* :

**-s** LeNomDuFichier pour la source(Entrer)  \
**-o** LeNomDuFichier pour output(Sortie)

**Deuxieme ajouts** : *logger*

On a ajouter une information qui va permettre de retourner les informations en cas de probleme dans le script ou bien savoir si ça marche.

```PYTHON
logging.info('On retourne que ça marche bien')
```

Sinon on retourne une erreur

```PYTHON
try:
    logging.info('On retourne que ça marche bien')
except Exception as e:  #EN CAS D'ERREUR
        logging.error(e)
```