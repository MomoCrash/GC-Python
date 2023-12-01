import random
import os
from time import *
from Tools import *

# For Stats
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

width:int = 5
height:int = 5

empty_slot: list = []

class Range:
    """
    Permet de définir une position et de récupérer une zone (i,j) autour de celle-ci
    """
    def __init__(self, x: int, y: int, radius:int =3):
        self.x = x
        self.y = y
        self.radius = radius
        
    def set_position(self, coord: tuple[int, int]):
        self.x = coord[0]
        self.y = coord[1]
        
    def min_max_x(self, width: int):
        min_x: int = self.x-self.radius
        max_x: int = self.x+self.radius
        if min_x < 0: min_x = 0
        if max_x > width: max_x = width
        return (min_x, max_x)
    
    def min_max_y(self, height: int):
        min_y: int = self.y-self.radius
        max_y: int = self.y+self.radius
        if min_y < 0: min_y = 0
        if max_y > height: max_y = height
        return (min_y, max_y)


############## GRID MANAGMENT ##################
def generate_grid() -> list:
    grid: list = []
    
    for i in range(height):
        grid.append([])
        for j in range(width):
            empty_slot.append((i, j))
            grid[i].append(" ")
            
    return grid

def pop_filled_slot(index: int):
    """ Supprime un élément à l'index """
    empty_slot[index]=empty_slot[-1]
    empty_slot.pop()


def remove_filled_slot(tpl: tuple[int, int]):
    """ Supprime un élément par correspondance """
    empty_slot.remove(tpl)
    
############# INPUT / OUTPUT MANAGMENT ##########
def print_score(player: int, computer: int):
    print("Score du joueur : " + str(player) + "\nScore de l'ordinateur : " + str(computer))


def print_grid(grid):
    string: str = ""
    for line in grid:
        for case in line:
            string += "[" + case + "]"
        string += "\n" 
    print(string)


def ask_position(question: str, grid: list)->list:
    """ Permet de demander à l'utilisateur une position sur la grisse d'ordre x+1 et y+1 """
    reponse: str = input(question)
    reponse: list = reponse.split(":")
    
    while True:
        
        try:
            x: int = int(reponse[0])
            y: int = int(reponse[1])
            
            if (x > 0 and x <= width) and (y > 0 and y <= height):
                if (grid[x-1][y-1] == " "):
                    return (x-1, y-1)
                
                else:
                    print("Quelqu'un a déjà joué ici !")
                    
            else:
                print("Votre placement est hors des limites de la grille !")
                
        except:
            print("Votre position n'existe pas essayez par exemple : 1:1.")
        reponse: list = input(question).split(":")
    
################ WIN PART ##################
def out_of_grid(i, j):
    """ Verifie si i OU j est hors de la map """
    return (i >= height or j >= width or i < 0 or j < 0)


def win_combinaison(grid, i, j, k, symbol, pattern: tuple[int, int, int, int]=(0,0,0,0)) -> bool:
    """ Permet de trouver si une combinaison est gagnant pour le symbole choisit avec un pattern
    Args:
        grid (list): La grille de jeu
        i (int): la position en colonne
        j (int): la position en ligne
        k (int): en k coup gagnant
        symbol (str): symbole du joueur qu'on verifie
        pattern (tuple, optional): Le patterne des ligne ou colonne à incrémenté. \n Exemple: (0, 1, 0, 1) -> Trouve une combinaison sur la ligne

    Returns:
        bool: le symbole a gagné 
    """
    symbol_count = 1
    for incr in range(1, k):
        if out_of_grid(i+(incr*pattern[0]), j+(incr*pattern[1])): break
        if grid[i+(incr*pattern[0])][j+(incr*pattern[1])] != symbol:
            break
        else:
            symbol_count += 1
    for decr in range(1, k):
        if out_of_grid(i-(decr*pattern[2]), j-(decr*pattern[3])): break
        if grid[i-(decr*pattern[2])][j-(decr*pattern[3])] != symbol:
            break
        else:
            symbol_count += 1
    return symbol_count >= k


def win_check(grid: list, k: int, symbol: str, last_position: Range=None) -> bool:
    """ Vefifie si un symbole a gagné """
    if last_position is None: return False
    
    if win_combinaison(grid, last_position.x, last_position.y, k, symbol, (0, 1, 0, 1)): return True
    if win_combinaison(grid, last_position.x, last_position.y, k, symbol, (1, 0, 1, 0)): return True
    if win_combinaison(grid, last_position.x, last_position.y, k, symbol, (1, 1, 1, 1)): return True
    if win_combinaison(grid, last_position.x, last_position.y, k, symbol, (-1, 1, -1, 1)): return True
    return False

################ IA PART ##################
def getRandomGridPosition() -> tuple:
    random_index: int = random.randint(0, len(empty_slot)-1)
    return (random_index, empty_slot[random_index])


def find_best_play(grid: list, k: int, symbol: str, last_position: Range=None) -> tuple[int, int]:
    """ Cherche le meilleure placement pour le symbole

    Args:
        grid (list): La grille de jeu
        k (int): Le nombre de coup
        symbol (str): Le symbole à verfier
        last_position (Range, optional): La dernière position joué

    Returns:
        tuple[int, int]: La position optimale
    """
    if last_position is None: return (False, (0,0))
    min_y, max_y = last_position.min_max_y(height)
    min_x, max_x = last_position.min_max_x(width)
    
    for i in range(min_y, max_y):
        for j in range(min_x, max_x):
            # Lines
            if  win_combinaison(grid, i, j, k, symbol, (0, 1, 0, 1)):
                return (i, j)
            # Column
            if win_combinaison(grid, i, j, k, symbol, (1, 0, 1, 0)):
                return (i, j)
            # Right Diagonal
            if win_combinaison(grid, i, j, k, symbol, (1, 1, 1, 1)):
                return (i, j)
            #Left Diagonal
            if win_combinaison(grid, i, j, k, symbol, (-1, 1, -1, 1)):
                return (i, j)  
    return (0,0)


def playIA(grid: list, k: int, last_position: Range=None) -> tuple[int, int]:
    
    isPlaced: bool = False
    best_position: tuple = (0, 0)
    
    best_win: tuple[int, int] = find_best_play(grid, k, "o", last_position)
    if best_win != (0, 0):
        print("WIN")
        best_position = best_win
        isPlaced = True
    else:
        best_block: tuple[int, int] = find_best_play(grid, k, "x", last_position)
        if best_block != (0, 0):
            print("BLOCK")
            best_position = best_block
            isPlaced = True
    
    if not isPlaced or grid[best_position[0]][best_position[1]] != " " or last_position is None:
        random_index, pos = getRandomGridPosition()
        pop_filled_slot(random_index)
        grid[pos[0]][pos[1]] = "o"
        return pos
        
    else:
        grid[best_position[0]][best_position[1]] = "o"
        remove_filled_slot((best_position[0], best_position[1]))
        return (best_position[0], best_position[1])
    
def game_loop(grid: list, k: int) -> tuple:
    """ La boucle de jeu principale """
    last_play: Range = Range(0, 0, 5)
    while True:
        # Player play turn
        position: list = ask_position("Mettez la position sour la forme 'x:y' : ", grid) # On demande une position au joueur
        remove_filled_slot((position[0], position[1])) # On enleve la case joué des cases jouables
        grid[position[0]][position[1]] = "x" # On le met sur la grille
        last_play.set_position(position) # On met le dernier coup joué sur le coup du joueur
        
        # On cheche une égalité ou une victoire pour x
        isWon = win_check(grid, k, "x", last_play)
        if isWon:
            print_grid(grid)
            print("X a gagné la partie !!")
            return ("x", checkAns("", ["Y", "N", "y", "n"], "Souhaitez-vous rejouer ? (y,n) : "))
        if len(empty_slot) == 0:
            print("Egalité !")
            return ("x", checkAns("", ["Y", "N", "y", "n"], "Souhaitez-vous rejouer ? (y,n) : "))
            
        # IA Play turn
        start = time()
        psoition_computer = playIA(grid, k, last_play) # On fait jouer l'IA
        print("Temps de jeu de l'IA :", time()-start)
        last_play.set_position(psoition_computer)
        
        # On affiche la grille avec les coups des deux joueurs
        print_grid(grid)
        
        # On cheche une égalité ou une victoire pour o
        isWon = win_check(grid, k, "o", last_play)
        if isWon:
            print_grid(grid)
            print("O a gagné la partie !!")
            return ("o", checkAns("", ["Y", "N", "y", "n"], "Souhaitez-vous rejouer ? (y,n) : "))
        if len(empty_slot) == 0:
            print("Egalité !")
            return ("x", checkAns("", ["Y", "N", "y", "n"], "Souhaitez-vous rejouer ? (y,n) : "))
 
def init_game():
    last_winner: str = "o"
    player_score: int = 0
    computer_score: int = 0
    coups: int = 0
    while True:
        global width
        global height
        width = ask_int("Entrez la largeur de la grille : ")
        height = ask_int("Entrez la hauteur de la grile : ")
        
        coups = ask_int(f"En combien de coup voulez-vous jouer (Entre 3 et {height}) : ")
        
        empty_slot.clear()
        gridPlay = generate_grid()
        
        #test_exec(gridPlay, 10000)
        #return
        
        if last_winner == "x": playIA(gridPlay, coups, None)
        print_grid(gridPlay)
        winner, replay = game_loop(gridPlay, coups)
        
        last_winner = winner
        if winner == "x":
            player_score += 1
        elif winner == "o":
            computer_score += 1
        print_score(player_score, computer_score)
        
        if not replay:
            os.system('python __init__.py')

def test_exec(grid, n):
    x: list = []
    y: list = []
    last_play: Range = Range(0, 0, 5)
    moyenne: int = 0
    pre_stat: float = time()
    for i in range(n):
        random_index, pos = getRandomGridPosition()
        pop_filled_slot(random_index)
        grid[pos[0]][pos[1]] = "x"
        last_play.set_position(pos)
        now = time()
        psoition_computer = playIA(grid, 3, last_play)
        turnTime = time() - now
        moyenne += turnTime
        last_play.set_position(psoition_computer)
        if i%1000 == 1:
            y.append(moyenne/1000)
            x.append(i)
            moyenne = 0
            
    print(f'Elapsed time : {time() - pre_stat} | Occurences : {n}' )
    x = np.array(x)
    y = np.array(y)
    
    X_Y_Spline = make_interp_spline(x, y)
 
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)
    
    plt.plot(X_, Y_)  
    plt.xlabel('x - turn')
    plt.ylabel('y - time')
    plt.title('Time by turn')
    plt.show()

if __name__ == '__main__':
    init_game()