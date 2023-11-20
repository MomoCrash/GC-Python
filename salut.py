import random

max: int = 100
min: int = 0
computer_number: int = 0
user_input: int = 0
started: bool = False
        
def is_type(object, typeof):
    return type(object) is typeof

while True:
    
    if not started:
        print("Bienvenue sur Plus ou Moins !")
        print("Durant le jeu vous pouvez à tout moment lors d'une question taper \n'Q' pour quitter \n'R' pour recommencer")
        max = int(input("Pour commencer donner la borne maximal de jeu (Un nombre) : "))
        min = int(input("Et maintenant la borne minimal : "))
    
        if max < min:
            print("Vous devez mettre une borne minimal plus petite que la maximal")
        else:
            computer_number = random.randrange(min, max)
            started = True
    else:
        user_input: object = input("Entre le chiffre de ton choix entre {min} et {max} : ".format(min=str(min), max=str(max)))
        
        if is_type(user_input, int):
            user_input: int = user_input
            
            if user_input > max:
                print("Vous êtes au dessus de la borne maximal {max}".format(max=max))
            if user_input < min:
                print("Vous êtes en dessous de la borne minimal {min}".format(min=min))
            elif user_input == computer_number:
                print("Tu l'as trouvé bien jouer tape 'R' pour rejouer")
            elif user_input > computer_number:
                print("Le chiffre à trouver est plus petit que {current}.".format(current=user_input))
            else:
                print("Le chiffre à trouver est plus grand que {current}.".format(current=user_input))
            continue
        
        if is_type(user_input, str):
            user_input: str = user_input
            if user_input == "Q" or user_input == "q":
                print("A très vite bébé.\n\n\n")
                exit()
            elif user_input == "R" or user_input == "r":
                print("Redémarrage du jeu !\n\n\n")
                started = False
            else:
                print("Votre réponse n'es pas bonne ! \nPour rappel les commandes sont :\n'Q' pour quitter \n'R' pour recommencer")
            continue


