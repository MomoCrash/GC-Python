import random
valeurs: dict = {"pierre":"ciseaux","feuille":"pierre","ciseaux":"feuille"}
pc: list = ["pierre","feuille","ciseaux"]
rejouer: bool = True

while rejouer : 
    pcChoice = random.choice(pc)
    player: str = input("pierre, feuille ou ciseaux ?")
    
    while player != "pierre" and player !="feuille" and player!="ciseaux":
        player: str = input("Pierre, feuille ou ciseaux ?")  
        
    for i,j in valeurs.items():
        if player==i and pcChoice==j:
            print("L'ordinateur a choisi :",pcChoice,"vous avez gagné !")
        elif player==j and pcChoice==i:
            print("L'ordinateur a choisi :",pcChoice,"vous avez perdu, dommage !")   
             
    if player == pcChoice :
         print("L'ordinateur a choisi :",pcChoice,"égalité")
         
    rejouer = input("Voulez-vous rejouer ? y/n ") == "y"
    
