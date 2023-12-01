from Tools import checkAns
import os

if __name__ == '__main__':
    game = checkAns("", ["pfc", "poum", "morp", "wordle", "quit"], "Quelle jeu voulez-vous lancer ? \nLes mots clés de lacement sont : \nPlus ou Moins: poum \nPierre Feuille Ciseau: pfc \nMorpion: morp \nWordle: wordle \nPour quitter: quit \nRéponse : ")
    if game == "pfc":
        os.system('python pfc.py')
    if game == "poum":
        os.system('python plus_ou_moins.py')
    if game == "morp":
        os.system('python tictactoe.py')
    if game == "wordle":
        os.system('python Wordle.py')
    if game == "quit":
        exit()