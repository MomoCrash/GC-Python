import random
from time import sleep
from Tools import ask_int 

def game_init():
    print("Bienvenue sur Plus ou Moins !")
    print("Durant le jeu vous pouvez à tout moment lors d'une question taper \n'Q' pour quitter \n'R' pour recommencer")
    max = ask_int("Pour commencer donner la borne maximale de jeu (Un nombre) : ")
    min = ask_int("Et maintenant la borne minimale : ", max)
    essais_max = ask_int("En combiens d'essais voulez-vous jouer ? : ")
    
    computer_number: int = random.randrange(min, max)
    rapport = game_instance(max, min, computer_number, essais_max)
    if rapport[0]:
        print("Bravo tu as trouvé la bonne réponse en {essais} essai(s) c'était {nbr}".format(essais=rapport[1], nbr=computer_number))
        sleep(2)
        print("Relancement du jeu.")
    else:
        print("Vous avez perdu !! \n Le jeu va se relancer !")

def game_instance(max, min, toFind, maxEssai):
    user_input = None
    essais = 0
    while toFind != user_input and essais <= maxEssai:
        user_input: object = input("Entre le chiffre de ton choix entre {min} et {max} : ".format(min=str(min), max=str(max)))
        
        try: 
            user_input: int = int(user_input)
            
            if user_input > max:
                print("Vous êtes au dessus de la borne maximale {max}".format(max=max))
            elif user_input < min:
                print("Vous êtes en dessous de la borne minimale {min}".format(min=min))
            elif user_input > toFind:
                print("Le chiffre à trouver est plus petit que {current}.".format(current=user_input))
                essais += 1
            elif user_input < toFind:
                print("Le chiffre à trouver est plus grand que {current}.".format(current=user_input))
                essais += 1
        
        except ValueError:
            user_input: str = user_input
            if user_input == "Q" or user_input == "q":
                print("A très vite ma jolie.\n\n\n")
                exit()
            elif user_input == "R" or user_input == "r":
                return (False, 0)
            else:
                print("Votre réponse n'es pas bonne ! \nPour rappel les commandes sont :\n'Q' pour quitter \n'R' pour recommencer")
        
    return (essais <= maxEssai, essais)

while True:
    game_init()