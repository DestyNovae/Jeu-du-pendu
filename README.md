# JEU DU PENDU

Bienvenue dans le projet "Jeu du Pendu" créé par DestyNovae! Ce projet est une implémentation du classique jeu de devinettes où les joueurs essaient de deviner un mot en proposant des lettres.

## Description

Ce jeu du pendu est un programme en Python qui permet aux utilisateurs de deviner un mot caché en entrant des lettres une par une. Pour chaque lettre incorrecte, une partie du pendu est dessinée. Le jeu se termine lorsque le mot est entièrement deviné ou que le pendu est complètement dessiné.

## Fonctionnalités

- Choix aléatoire de mots à partir d'un fichier XML.
- Affichage de la potence et des lettres déjà devinées.
- Gestion des lettres accentuées.
- Messages d'erreur pour les lettres déjà devinées ou les entrées invalides.
- Affichage du résultat final avec la possibilité de voir la définition du mot (si disponible).

## Prérequis

- Python 3.x
- Fichier `dictionnaire.xml` contenant les mots.

## Installation

1. Clonez le dépôt GitHub :

    ```bash
    git clone https://github.com/DestyNovae/jeu-du-pendu.git
    cd jeu-du-pendu
    ```

2. Assurez-vous d'avoir le fichier `dictionnaire.xml` dans le répertoire du projet. Voici un exemple de l'architecture du fichier XML :

    ```xml
        </mot>
        <mot mot="python" nb="1" id="python">
            <entree ligne="112230">
               <M mot="python" mot-initial="python"/>
               <CONT>an mov sol</CONT>
               <DOM nom="reptiles">REP</DOM>
               <OP>rept</OP>
               <SENS>serpent aglyphe grd</SENS>
               <OP1>M1a1</OP1>
               <CA categorie="N" type="animal" genre="M">-8</CA>
            </entree>
        </mot>
        <!-- Ajoutez d'autres mots ici -->
    ```

## Utilisation

Exécutez le script Python pour démarrer le jeu.

Windows :
  ```python
  py .\Pendu.py
  ```

Linux :
  ```python
  py ./Pendu.py
  ```

Suivez les instructions à l'écran pour deviner les lettres du mot caché.
Vous pouvez deviner une lettre à la fois.
Si la lettre est correcte, elle apparaîtra dans le mot.
Si elle est incorrecte, une partie du pendu sera dessinée.

## Exemple de Jeu

![image](https://github.com/DestyNovae/Jeu-du-pendu/assets/152598490/46c6787a-8d2f-4399-8dfa-78293a59b625)

## Contribuer

Les contributions sont les bienvenues! Si vous avez des idées d'améliorations ou des bugs à signaler, veuillez ouvrir une issue ou soumettre une pull request.

## Auteur

DestyNovae
