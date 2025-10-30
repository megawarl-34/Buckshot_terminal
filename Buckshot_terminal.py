import random

joueur_actuel = 1

def charger_revolver():
    chargeur = [1, 0, 0, 0, 0, 0,] #Taille de la list = nombre de balle total. 0 = balle a blanc / 1 = vrai balle
    random.shuffle(chargeur)
    return chargeur

def tirer(chargeur):
    balle = chargeur.pop(0)
    
    if balle == 1:
        print("BOOM ! \n")
        
    else:
        print("*clic*... *rien ne se passe* \n")
    return balle, chargeur

chargeur = charger_revolver()

while True:
    print(f"\n--- Tour du joueur {joueur_actuel} ---")
    
    cmd = input("Tape 'Tire' pour tirer, 'quit' pour quitter >").lower().strip()
    if cmd in ("tire", "tirer"):
        cible = input(f"Sur qui veux-tu tirer ? (1 ou 2) > ").strip()
        
        balle, chargeur = tirer(chargeur)
        
        if balle is None:
            break
        
        if balle == 1:
            if cible == str(joueur_actuel):
                gagnant = 2 if joueur_actuel == 1 else 1
                print(f"Le joueur {joueur_actuel} est mort ! Le joueur {gagnant} gagne ! \n")
            else:
                print(f"Le joueur {cible} est mort ! Le joueur {joueur_actuel} gagne ! \n")
            break
    
        else:
            if cible == str(joueur_actuel):
                print(f"Le joueur {joueur_actuel} a survécu et rejoue.")
            else:
                if joueur_actuel == 1:
                    joueur_actuel = 2
                else:
                    joueur_actuel = 1
                print(f"C'est maintenant au joueur {joueur_actuel} de jouer.")
        
    elif cmd in ("quit", "q", "exit"):
        break
    
    else:
        print("Commande inconnue. Tape 'Tire' ou 'quit'.")