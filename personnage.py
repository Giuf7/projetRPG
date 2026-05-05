import random

# Initialisation des variables
nom = str(input("Quel est le nom de ton personnage ? : "))
atk = random.randrange(10,20)
hp = random.randrange(100,120)
inventaire = []

def creation_personnage():
    global nom, atk, hp, inventaire
    
    nom
    atk
    hp
    inventaire
    print(f"\nBienvenue, {nom} ! Ton aventure commence maintenant.")

def afficher_stats():
    print(f"--- Stats de {nom} ---")
    print(f"Points de vie : {hp}")
    print(f"Attaque : {atk}")
    print(f"Inventaire : {inventaire}")
    print("----------------------")

def afficher_inventaire():
    print(f"Inventaire: {inventaire}")
