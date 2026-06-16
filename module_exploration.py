from combat import combattreMonstre1, combattreMonstre2
from enigmes import resoudre_enigme_est, resoudre_enigme_ouest

def deplacer() :
    direction = input("Où allez-vous ? ")
    match direction.lower():
        case "nord":
            combattreMonstre1()
        case "sud":
            combattreMonstre2()
        case "est":
            resoudre_enigme_est()
        case "ouest":
            resoudre_enigme_ouest()
        case _:
            print("Mauvaise destination")

def  afficher_salle(rencontre) :
    if rencontre == "Combat" :
        print("")
    if rencontre == "Enigme" : 
        print("")
