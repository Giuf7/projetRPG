# projetRPG
## Division du travail
### Giuseppe : Perso et stats

HP et ATK

### Alex :  Exploration/Salles

Salles (spawn + N/S/E/O)

### Logan : Objets et énigmes
énigmes simples avec input, si énigme réussie --> potion

### Louis : Combat
créer ennemis + système de combat
premier tour random

#Module Exploration / Salles
Alexandre Hoppe | Crée un dictionnaire, et deux functions.
Le dictionnaire (sallesDictionnaire) contient quatre salles et est defini si la salle contien une enigme ou un ennemi.
La première fonction (deplacer()) demande la direction prise, verifie si la reponse est une des 4 direction (nord, sud, est, ouest), et renvoi le contenu de la salle, en utilisant le dictionnaire : sallesDictionnaire.
La deuxième fonction utilise le contenu de la salle defini par la fonction deplacer() pour appeller la fonction combattre() ou la fonction resoudre_enigme().