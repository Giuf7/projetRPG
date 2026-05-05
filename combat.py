from personnage import hp, atk, nom
import random

#Ajout des stats des monstres
atkMonstre1 = 10
hpMonstre1 = 40
nomMonstre1 = "Guerrier gobelin"

atkMonstre2 = 5
hpMonstre2 = 30
nomMonstre2 = "Bandit"

#Création de la fonction pour combattre le premier monstre
def combattreMonstre1():
    joueurhp = hp
    joueuratk = atk
    joueurnom = nom
    monstreHP = hpMonstre1
    monstreATK = atkMonstre1
    monstreNom = nomMonstre1
    randomCommence = random.randint (1,2)
    if randomCommence == 2:
            tour = True
            print("Le joueur commence")
    else:
            print("Le monstre commence!")
            tour = False


    while joueurhp > 0 and monstreHP > 0:
        print(f"{joueurnom} est attaqué par {monstreNom}!!")
        while tour:
            print(f"{joueurnom} attaque {monstreNom} pour {joueuratk} dégâts.")
            monstreHP = monstreHP - joueuratk
            print(f"Le monstre a {monstreHP} points de vie restants, il se prépare à attaquer...")
            tour = not tour
        else:
             print(f"Le monstre attaque {joueurnom} pour {monstreATK} dégâts.")
             joueurhp = joueurhp - monstreATK
             print(f"{joueurnom} a {joueurhp} points de vie restants. À votre tour!")
             tour = not tour
    else:
        if monstreHP <= 0:
            print("Le monstre est vaincu!")
        elif joueurhp <= 0:
             print("Le monstre a gagné!")

#Création de la fonction pour combattre le 2e monstre
def combattreMonstre2():
    joueurhp = hp
    joueuratk = atk
    joueurnom = nom
    monstreHP = hpMonstre2
    monstreATK = atkMonstre2
    monstreNom = nomMonstre2
    randomCommence = random.randint (1,2)
    if randomCommence == 2:
            tour = True
            print("Le joueur commence")
    else:
            print("Le monstre commence!")
            tour = False


    while joueurhp > 0 and monstreHP > 0:
        print(f"{joueurnom} est attaqué par {monstreNom}!!")
        while tour:
            print(f"{joueurnom} attaque {monstreNom} pour {joueuratk} dégâts.")
            monstreHP = monstreHP - joueuratk
            print(f"Le monstre a {monstreHP} points de vie restants, il se prépare à attaquer...")
            tour = not tour
        else:
             print(f"Le monstre attaque {joueurnom} pour {monstreATK} dégâts.")
             joueurhp = joueurhp - monstreATK
             print(f"{joueurnom} a {joueurhp} points de vie restants. À votre tour!")
             tour = not tour
    else:
        if monstreHP <= 0:
            print("Le monstre est vaincu!")
        elif joueurhp <= 0:
             print("Le monstre a gagné!")