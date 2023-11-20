import random
valeurs: dict = {"pierre":"ciseaux","feuille":"pierre","ciseaux":"feuille"}
pc: list = ["pierre","feuille","ciseaux"]
rejouer: bool = True

while rejouer : 
    pcChoice = random.choice(pc)
    player: str = input("pierre, feuille ou ciseaux ?")
        
    for i,j in valeurs.items():
        if player==i and pcChoice==j:
            print("pc chose",pcChoice,"you won")
        elif player==j and pcChoice==i:
            print("pc chose",pcChoice,"you lose")    
    if player == pcChoice :
         print("pc chose",pcChoice,"draw")
    rejouer = input("veux-tu rejouer ? y/n") == "y"
    
