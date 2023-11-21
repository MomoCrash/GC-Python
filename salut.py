import random

max: int = 100
min: int = 0
computer_number: int = 0
user_input: int = 0
started: bool = False
essais: int = 0

def ask_int(question):
    
    reponse=""
    while not reponse.isdigit():
        reponse = input(question)
    return int(reponse)

while True:
    
    if not started:
        print("Bienvenue sur Plus ou Moins !")
        print("Durant le jeu vous pouvez à tout moment lors d'une question taper \n'Q' pour quitter \n'R' pour recommencer")
        max = ask_int("Pour commencer donner la borne maximale de jeu (Un nombre) : ")
        min = ask_int("Et maintenant la borne minimale : ")
    
        if max < min:
            print("Vous devez mettre une borne minimale plus petite que la maximal")
        else:
            computer_number: int = random.randrange(min, max)
            started: bool = True
    else:
        user_input: object = input("Entre le chiffre de ton choix entre {min} et {max} : ".format(min=str(min), max=str(max)))
        
        try: 
            user_input: int = int(user_input)
            
            if user_input > max:
                print("Vous êtes au dessus de la borne maximale {max}".format(max=max))
            elif user_input < min:
                print("Vous êtes en dessous de la borne minimale {min}".format(min=min))
            elif user_input == computer_number:
                print("Bravo tu as trouvé la bonne réponse en {essais} essai(s) c'était {nbr}".format(essais=essais, nbr=user_input))
                print("Relancement du jeu.")
                started = False
            elif user_input > computer_number:
                print("Le chiffre à trouver est plus petit que {current}.".format(current=user_input))
                essais += 1
            else:
                print("Le chiffre à trouver est plus grand que {current}.".format(current=user_input))
                essais += 1
            continue
        
        except ValueError:
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