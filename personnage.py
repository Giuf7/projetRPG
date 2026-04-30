atk = 10
hp = 100
inventaire = []
nom = str(input("Quel est le nom de votre personnage ?:"))

def afficher_stats():
    print(f"{nom}: Vous avez {hp} point de vue et {atk} d'attaque.")
    print(f"Votre inventaire: {inventaire}")
