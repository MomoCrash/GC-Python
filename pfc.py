import os
import random
from Tools import checkAns

values: list = [["égalité","vous avez perdu, dommage !","vous avez gagné !"],
                ["vous avez gagné !","égalité","vous avez perdu, dommage !"],
                ["vous avez perdu, dommage !","vous avez gagné !","égalité"]]
valToInt: dict = {"pierre": 0, "feuille": 1, "ciseaux": 2}
pc: list = ["pierre","feuille","ciseaux"]
replay: bool = True

def game_instance(options,listVal):
    """ Lance une instance d'une partie de pierre feuille ciseau"""
    botChoice = random.choice(options)
    plChoice: str = input("Pierre, feuille ou ciseaux ?")
    
    plChoice = checkAns(plChoice, pc, "pPierre, feuille ou ciseaux ? : ")
    
    intBotChoice = listVal[botChoice]
    plChoice = listVal[plChoice]
    return botChoice,plChoice,intBotChoice

def print_play(val,pcChoice,player,intPc):
    """ Affiche ce que l'ordinateur a joué """
    print(f"L'ordinateur a choisi : {pcChoice} \nRésultats :\n{val[player][intPc]}")

if __name__ == '__main__':
    while replay : 
        bot,p,intBot=game_instance(pc,valToInt)
        
        print_play(values,bot,p,intBot)
            
        replay = input("Voulez-vous rejouer ? y/n : ") == "y"
    os.system('python __init__.py')
