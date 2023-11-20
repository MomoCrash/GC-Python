import random
valeurs: dict = {"pierre":"ciseaux","feuille":"pierre","ciseaux":"feuille"}
pc: list = ["pierre","feuille","ciseaux"]
rejouer: bool = True

#isnot_FPC(joueur):
#    return joueur!="pierre" and joueur !="fauille" and joueur !="ciseaux"

while rejouer : 
    pcChoice = random.choice(pc)
    player: str = input("Pierre, feuille ou ciseaux ? ")
    
    while player!="pierre" and player !="feuille" and player !="ciseaux":
        player: str = input("Pierre, feuille ou ciseaux ?")  
        
    for i,j in valeurs.items():
        if player==i and pcChoice==j:
            print("L'ordinateur a joué",pcChoice,"vous avez gagné !")
        elif player==j and pcChoice==i:
            print("L'ordinateur a joué",pcChoice,"vous avez perdu, dommage.")   
             
    if player == pcChoice :
         print("L'odinateur a joué",pcChoice,"égalité")
         
    rejouer = input("Entrez 'R' pour rejouer : ") == "y"
    