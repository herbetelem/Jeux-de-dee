# Here I import the lib i will need to use
###############################################################################################################
import random
import re
###############################################################################################################

# This function is here to check the name
###############################################################################################################
def chooseName(compteur, listJoueur):
    joueurX = input("Joueur " + str((compteur + 1)) + ", quel est ton nom ? ")
    if joueurX == "":
        joueurX = print("Veuillez saisir quelque chose ! ")
        return "ko"
    if re.match("^[0-9_-]*$", joueurX):
        joueurX = print("Veuillez ne pas choisir de chiffre ! ")
        return "ko"
    if joueurX in listJoueur:
        print("C'est malheureux mais un joueur porte deja ce nom, veuillez en prendre un autre ! ")
        return "ko"
    else:
        return joueurX
###############################################################################################################

# I set up my game into a function for calling her at the end if the player want to play again
###############################################################################################################
def jeuxDeDee():
###############################################################################################################

# Here i write the rules of the games
###############################################################################################################
    print()
    print("Jeu de dés")
    print("----------")
    print()

    print("Plusieurs Joueurs lancent chacun des dés (lancement automatique par le programme)")
    print("Celui qui obtient le plus haut score est déclaré gagnant.")
    print("En cas de scores égaux, ils sont déclarés ex aequo.")
###############################################################################################################

# Here I ask how many player will play
###############################################################################################################
    print()
    nbJoueurs = input("Combien de joueurs êtes vous ? ")
    while re.match("^[A-Za-z]*$", nbJoueurs):
        nbJoueurs = input("veuillez choisir un chiffre ! ")
    while int(nbJoueurs) < 2 or int(nbJoueurs) > 10:
        nbJoueurs = int(input("Veuillez choisir un nombre entre 2 et 10 ? "))
###############################################################################################################

# Here I ask the name of all player and check if they are good, then i add the name on my list
###############################################################################################################
    print()
    listJoueur = []
    compteur = 0
    while int(compteur) < int(nbJoueurs):
        joueurX = chooseName(compteur, listJoueur)
        while joueurX == "ko":
            joueurX = chooseName(compteur, listJoueur)
        listJoueur.append(joueurX)
        print("Bonjour " + str(listJoueur[compteur]) + " !")
        compteur = compteur + 1
###############################################################################################################

# Here I ask how many face the dice will have and I check if they are one of thoose I propose
###############################################################################################################
    print()
    print("Combien de face vos dées auront ? ")
    nbFace = int(input("Choisissez parmis 4, 6, 8, 10, 12, 20 ou 100 : "))
    deePossible = [4, 6, 8, 10, 12, 20, 100]
    while nbFace not in deePossible:
        print()
        nbFace = int(input("Veuillez prendre l'une de ces option 4, 6, 8, 10, 12, 20 ou 100 : "))
###############################################################################################################

# Here I ask how many Dice the player will have
###############################################################################################################
    print()
    print("Combien de dée aurez vous ? ")
    nbDee = int(input("Choisissez entre 1 et 10 : "))
    while nbDee < 1 or nbDee > 10:
        nbDee = int(input("Entre 1 et 10 pas moin ou plus merci : "))
###############################################################################################################

# Here I start to made the score of every player
###############################################################################################################
    print()
    compteur = 0
    bestScore = 0
    bestPlayer = ""
    result = 0
    while compteur < int(nbJoueurs):
        dee = 0
        scoreX = 0
        print()
        print(str(listJoueur[compteur]) + " Lance ces dées")
        while dee < nbDee:
            jetX = random.randint(1, int(nbFace))
            print(jetX)
            scoreX = scoreX + jetX
            dee = dee + 1
        if scoreX > bestScore:
            result = 0
            bestScore = scoreX
            bestPlayer = listJoueur[compteur]
        elif scoreX == bestScore:
            result = 1
            bestPlayer = bestPlayer + " et " + listJoueur[compteur]
        compteur = compteur + 1
    print()
###############################################################################################################

# Here I check is the result is a win of one player or two
###############################################################################################################
    if result == 0:
        print("c'est " + str(bestPlayer) + " qui gagne avec le score de " + str(bestScore))
    else:
        print(str(bestPlayer) + " ce partage la victoire avec le score de " + str(bestScore))
###############################################################################################################


# Here I ask if the player want to play again
###############################################################################################################
    print()
    replay = str(input("souhaitez vous relancer une partie ? oui ou non ? "))
    reponse = ["oui", "non"]
    while replay not in reponse:
        replay = str(input("veuillez repondre par oui ou non ! "))
    if replay == "oui":
        jeuxDeDee()
###############################################################################################################

# And here it's just for fun :)
###############################################################################################################
    else:
        print()
        print("     -------------------------------")
        print("     Merci d'avoir jouer au revoir !")
        print("     -------------------------------")
        print()
        print("                 ______")
        print("                /     /\ ")
        print("               /     /##\ ")
        print("              /     /####\ ")
        print("             /     /######\ ")
        print("            /     /########\ ")
        print("           /     /##########\ ")
        print("          /     /#####/\#####\ ")
        print("         /     /#####/++\#####\ ")
        print("        /     /#####/++++\#####\ ")
        print("       /     /#####/\+++++\#####\ ")
        print("      /     /#####/  \+++++\#####\ ")
        print("     /     /#####/    \+++++\#####\ ")
        print("    /     /#####/      \+++++\#####\ ")
        print("   /     /#####/        \+++++\#####\ ")
        print("  /     /#####/__________\+++++\#####\ ")
        print(" /                        \+++++\#####\ ")
        print("/__________________________\+++++\####/")
        print("\+++++++++++++++++++++++++++++++++\##/")
        print(" \+++++++++++++++++++++++++++++++++\/")
        print()
###############################################################################################################


# Here i call my game for the first time
###############################################################################################################
jeuxDeDee()
###############################################################################################################