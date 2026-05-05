sallesDictionnaire = {
    "nord" : "Combat",
    "sud" : "Combat",
    "est" : "Enigme",
    "ouest" : "Enigme"
}



def deplacer() :
    direction = input("Où allez-vous ? ")
    if direction.lower() == "nord" or  direction.lower() == "sud" or direction.lower() == "est" or  direction.lower() == "ouest":
        return  sallesDictionnaire[direction.lower()]
    else :
        print("Ce n'est pas une diretion")

def  afficher_salle(rencontre) :
    if rencontre == "Combat" :
        print("")
    if rencontre == "Enigme" : 
        print("")

rencontre = deplacer()
testvarible = afficher_salle(rencontre)
