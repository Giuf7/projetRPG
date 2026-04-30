#Ajout des stats des monstres
atkMonstre1 = 10
hpMonstre1 = 40
nomMonstre1 = "Guerrier gobelin"

atkMonstre2 = 5
atkMonstre2 = 30
nomMonstre2 = "Bandit"

joueurhp = 100
joueuratk = 10
joueurnom = "louis"
#Création de la fonction
import random
def combattreMonstre1():
    hp = joueurhp
    atk = joueuratk
    nom = joueurnom
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


    while hp > 0 and monstreHP > 0:
        print(f"{nom} est attaqué par {monstreNom}!!")
        while tour:
            print(f"{nom} attaque {monstreNom} pour {atk} dégâts.")
            monstreHP = monstreHP - atk
            print(f"Le monstre a {monstreHP} points de vie restants, il se prépare à attaquer...")
            tour = not tour
        else:
             print(f"Le monstre attaque {nom} pour {monstreATK} dégâts.")
             hp = hp - monstreATK
             print(f"{nom} a {hp} points de vie restants. À votre tour!")
             tour = not tour
    else:
        if monstreHP <= 0:
            print("Le monstre est vaincu!")
        elif hp <= 0:
             print("Le monstre a gagné!")
        
combattreMonstre1()