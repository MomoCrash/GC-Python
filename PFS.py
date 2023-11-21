import random
#[pierre[pierre,feuille,ciseaux],feuille[pierre,feuille,ciseaux],ciseaux[pierre,feuille,ciseaux]]
values: list = [["égalité","vous avez perdu, dommage !","vous avez gagné !"],
                ["vous avez gagné !","égalité","vous avez perdu, dommage !"],
                ["vous avez perdu, dommage !","vous avez gagné !","égalité"]]
valToInt: dict = {"pierre": 0, "feuille": 1, "ciseaux": 2}
pc: list = ["pierre","feuille","ciseaux"]
replay: bool = True

def checkAns(player_input):
    poss: list = ["pierre","feuille","ciseaux"]
    while True:
        for i in poss:
            if player_input==i:
                return player_input
        player_input = input("pierre, feuille ou ciseaux ?")

def gameInstance(options,listVal):
    
    botChoice = random.choice(options)
    plChoice: str = input("pierre, feuille ou ciseaux ?")
    
    plChoice = checkAns(plChoice)
    
    intBotChoice = listVal[botChoice]
    plChoice = listVal[plChoice]
    return botChoice,plChoice,intBotChoice

def play(val,pcChoice,player,intPc):
    
    print("L'ordinateur a choisi :",pcChoice,val[player][intPc])

while replay : 
    
    bot,p,intBot=gameInstance(pc,valToInt)
    
    play(values,bot,p,intBot)
         
    replay = input("Voulez-vous rejouer ? y/n ") == "y"
