#Ajout des stats des monstres
atkMonstre1 = 10
hpMonstre1 = 25
nomMonstre1 = "Guerrier gobelin"

atkMonstre2 = 5
atkMonstre2 = 30
nomMonstre2 = "Bandit"

#Création de la fonction
import random
def combattreMonstre1():
    monstreHP = hpMonstre1
    monstreATK = atkMonstre1
    monstreNom = nomMonstre1


    while hp != 0 or monstreHP != 0:
        print(f"{nom} est attaqué par {monstreNom}!!")
        randomCommence = random.randint (1,2)
        if randomCommence == 2:
            print("Le joueur commence")
        
        else:
            print("Le monstre commence!")
