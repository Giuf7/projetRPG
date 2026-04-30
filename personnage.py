# Initialisation des variables
nom = ""
atk = 0
hp = 0
inventaire = []

def creation_personnage():
    global nom, atk, hp, inventaire
    
    nom = str(input("Quel est le nom de ton personnage ? : "))
    atk = 10
    hp = 100
    inventaire = [""]
    print(f"\nBienvenue, {nom} ! Ton aventure commence maitenant.")

def afficher_stats():
    print(f"--- Stats de {nom} ---")
    print(f"Points de vie : {hp}")
    print(f"Attaque : {atk}")
    print(f"Inventaire : {inventaire}")
    print("----------------------")
