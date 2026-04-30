from personnage import inventaire

enigme_salle_est = "Je suis toujours devant toi, mais tu ne peux jamais me voir. Qui suis-je ?"
reponse_salle_est = "le futur"
enigme_salle_ouest = "Je peux être cassé sans jamais être touché. Qui suis-je ?"
reponse_salle_est = "le silence"
objet_salle_est = "potion"
objet_salle_ouest = "épée"


def prendre_objet_est():
    inventaire = objet_salle_est
    print(f"Vous avez ajouté {objet_salle_est} à votre inventaire")

def prendre_objet_ouest(): 
    inventaire = objet_salle_ouest
    print(f"Vous avez ajouté {objet_salle_ouest} à votre inventaire")

def resoudre_enigme_est ():
    print("Vous entrez dans la salle est et vous apercevez des écritures sur le mur du fond. Il s'agit d'une énigme !")
    print(enigme_salle_est)

    reponse_user_est = print(input("Quel est votre réponse ?: "))

    if reponse_salle_est == reponse_user_est: 
        print(f"C'est la bonne réponse. Une {objet_salle_est} tombe au sol.")
        reponse_ramassage_objet =  bool(print(input("Voulez-vous la ramasser ? (True or False):")))
        if reponse_ramassage_objet:
            prendre_objet_est()
        else:
            print("Vous sortez de la salle sans prendre l'objet")
    else :
        print("C'est la mauvaise réponse, vous êtes expulsé de la salle")

def resoudre_enigme_ouest ():
    print("Vous entrez dans la salle ouest et vous apercevez des écritures sur le mur du fond. Il s'agit d'une énigme !")
    print(enigme_salle_ouest)

    reponse_user_ouest = print(input("Quel est votre réponse ?: "))

    if reponse_salle_est == reponse_user_ouest: 
        print(f"C'est la bonne réponse. Une {objet_salle_ouest} tombe au sol.")
        reponse_ramassage_objet =  bool(print(input("Voulez-vous la ramasser ? (True or False):")))
        if reponse_ramassage_objet:
            prendre_objet_ouest()
        else:
            print("Vous sortez de la salle sans prendre l'objet")
    else :
        print("C'est la mauvaise réponse, vous êtes expulsé de la salle")