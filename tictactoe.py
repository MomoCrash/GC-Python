import random
values: dict = {"pierre":"ciseaux","feuille":"pierre","ciseaux":"feuille"}
pc: list = ["pierre","feuille","ciseaux"]
replay: bool = True

def checkAns(player_input):
    poss: list = ["pierre","Pierre","feuille","Feuille","ciseaux","Ciseaux"]
    while True:
        for i in poss:
            if player_input==i:
                return player_input
        player_input = input("pierre, feuille ou ciseaux ?")

def gameInstance(options):
    
    botChoice = random.choice(options)
    pChoice: str = input("pierre, feuille ou ciseaux ?")
    
    pChoice = checkAns(pChoice)
    
    return botChoice,pChoice

def play(val,pcChoice,player):

    for i,j in val.items():
        if player==i and pcChoice==j:
            print("L'ordinateur a choisi :",pcChoice,"vous avez gagné !")
        elif player==j and pcChoice==i:
            print("L'ordinateur a choisi :",pcChoice,"vous avez perdu, dommage !")   
             
    if player == pcChoice :
         print("L'ordinateur a choisi :",pcChoice,"égalité")

while replay : 
    
    bot,p=gameInstance(pc)
    
    play(values,bot,p)
         
    replay = input("Voulez-vous rejouer ? y/n ") == "y"
