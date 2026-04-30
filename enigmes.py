
enigme_salle_est = "Je suis toujours devant toi, mais tu ne peux jamais me voir. Qui suis-je ?"
reponse_salle_est = "le futur"
enigme_salle_ouest = "Je peux être cassé sans jamais être touché. Qui suis-je ?"
reponse_salle_est = "le silence"
objet_salle_est = "potion"
objet_salle_ouest = "épée"

def prendre_objet():
    print("blabla")

def resoudre_enigme_est ():
    print("Vous entrez dans la salle est et vous apercevez des écritures sur le mur du fond. Il s'agit d'une énigme !")
    print(enigme_salle_est)

    reponse_user_est = print(input("Quel est votre réponse ?: "))

    if reponse_salle_est == reponse_user_est: 
        print(f"C'est la bonne réponse. Une {objet_salle_est} tombe au sol.")
        print("Voulez-vous la ramasser ?")
    else :
        print("C'est la mauvaise réponse, vous êtes expulsé de la salle")