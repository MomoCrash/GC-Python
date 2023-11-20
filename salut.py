import random

max: int = 100
min: int = 0
computer_number: int = 0
user_number: int = 0
started: bool = False

def game_loop():
    
    global max
    global min
    global computer_number
    global user_number
    global started
    
    if not started:
        print("Bienvenue sur Plus ou Moins !")
        print("Durant le jeu vous pouvez à tout moment lors d'une question taper \n 'Q' pour quitter \n 'R' pour recommencer")
        max = int(input("Pour commencer donner la borne maximal de jeu (Un nombre) : "))
        min = int(input("Et maintenant la borne minimal : "))
    
        if max < min:
            print("Vous devez mettre une borne minimal plus petite que la maximal")
        else:
            computer_number = random.randrange(min, max)
            started = True
    else:
        user_number = int(input("Entre le chiffre de ton choix entre {min} et {max} : ".format(min=str(min), max=str(max))))
        if user_number == computer_number:
            print("Tu l'as trouvé bien jouer tape 'R' pour rejouer")
        elif user_number > computer_number:
            print("Le chiffre à trouver est plus petit que {current}.".format(current=user_number))
        else:
            print("Le chiffre à trouver est plus grand que {current}.".format(current=user_number))
            
    game_loop()
        
game_loop()