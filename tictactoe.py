import random
from time import *
#import numpy as np
#from scipy.interpolate import make_interp_spline
#import matplotlib.pyplot as plt

WIDTH:int = 3
HEIGHT:int = 3
COUP_GAGNANT:int = 3

empty_slot = []
deleted_element = 0

class Range:
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
        if max_x > width: max_x = width-1
        return (min_x, max_x)
    
    def min_max_y(self, height: int):
        min_y: int = self.y-self.radius
        max_y: int = self.y+self.radius
        if min_y < 0: min_y = 0
        if max_y > height: max_y = height-1
        return (min_y, max_y)


############## GRID MANAGMENT ##################
def generateGrid()->list:
    
    grid: list = []
    
    for i in range(HEIGHT):
        grid.append([])
        for j in range(WIDTH):
            empty_slot.append((i, j))
            grid[i].append(" ")
            
    return grid

## Deletes slots that are already taken 
def popFilledSlot(index):
    empty_slot[index]=empty_slot[-1]
    empty_slot.pop()


def removeFilledSlot(tpl: tuple[int, int]):
    empty_slot.remove(tpl)
    
############# INPUT / OUTPUT MANAGMENT ##########
def printScore(player: int, computer: int):
    print("Score du joueur : " + str(player) + "\nScore de l'ordinateur : " + str(computer))


def printGrid(grid):
    
    string: str = ""
    for line in grid:
        for case in line:
            string += "[" + case + "]"
        string += "\n" 
    print(string)


def askReplay()->bool:
    
    valid_anwsers = ["Y", "y", "n", "N"]
    reponse = input("Voulez-vous rejouer ? Y/n : ")
    
    while reponse not in valid_anwsers:
        reponse = input("Voulez-vous rejouer ? Y/n : ")
    
    if reponse == "Y" or reponse == "y":
        return True
    
    else:
        return False


def askPosition(question: str, grid: list)->list:
    
    reponse: str = input(question)
        
    reponse: list = reponse.split(":")
    
    while True:
        
        try:
            x: int = int(reponse[0])
            y: int = int(reponse[1])
            
            if (x > 0 and x <= WIDTH) and (y > 0 and y <= HEIGHT):
                if (grid[x-1][y-1] == " "):
                    return (x-1, y-1)
                
                else:
                    print("Quelqu'un a déjà joué ici !")
                    reponse: list = input(question).split(":")
                    
            else:
                print("Votre placement est hors des limites de la grille !")
                reponse: list = input(question).split(":")
                
        except:
            print("Votre position n'existe pas essayez par exemple : 1:1.")
            reponse: list = input(question).split(":")
    
################ WIN PART ##################
def out_of_grid(i, j):
    return (i >= HEIGHT or j >= WIDTH or i < 0 or j < 0)


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
    if last_position is None: return False
    
    if win_combinaison(grid, last_position.x, last_position.y, k, symbol, (0, 1, 0, 1)): return True
    if win_combinaison(grid, last_position.x, last_position.y, k, symbol, (1, 0, 1, 0)): return True
    if win_combinaison(grid, last_position.x, last_position.y, k, symbol, (1, 1, 1, 1)): return True
    if win_combinaison(grid, last_position.x, last_position.y, k, symbol, (-1, 1, -1, 1)): return True
    return False

################ IA PART ##################
def getRandomGridPosition()->tuple:
    random_index: int = random.randint(0, len(empty_slot)-1)
    return (random_index, empty_slot[random_index])


def find_best_play(grid: list, k: int, symbol: str, last_position: Range=None) -> tuple[int, int]:
    if last_position is None: return (False, (0,0))
    min_x, max_x = last_position.min_max_x(WIDTH)
    min_y, max_y = last_position.min_max_y(HEIGHT)
    
    for i in range(min_y, max_y):
        for j in range(min_x, max_x):
            print(i, j)
            print(win_combinaison(grid, i, j, k, symbol, (0, 1, 0, 1)))
            # Lines
            if  win_combinaison(grid, i, j, k, symbol, (0, 1, 0, 1)):
                return (i, j)
            # Column
            elif win_combinaison(grid, i, j, k, symbol, (1, 0, 1, 0)):
                return (i, j)
            # Right Diagonal
            elif win_combinaison(grid, i, j, k, symbol, (1, 1, 1, 1)):
                return (i, j)
            #Left Diagonal
            elif win_combinaison(grid, i, j, k, symbol, (-1, 1, -1, 1)):
                return (i, j)  
    return (0,0)


def playIA(grid: list, k: int, last_position: Range=None) -> tuple[int, int]:
    
    isPlaced: bool = False
    best_position: tuple = (0, 0)
    
    best_win = find_best_play(grid, k, "o", last_position)
    if best_win != (0, 0):
        best_position = best_win
        isPlaced = True
    else:
        best_block = find_best_play(grid, k, "x", last_position)
        if best_block != (0, 0):
            best_position = best_block
            isPlaced = True
    
    if not isPlaced or grid[best_position[0]][best_position[0]] != " " or last_position is None:
        print("Random play for IA")
        random_index, pos = getRandomGridPosition()
        popFilledSlot(random_index)
        grid[pos[0]][pos[1]] = "o"
        return pos
        
    else:
        grid[best_position[0]][best_position[1]] = "o"
        removeFilledSlot((best_position[0], best_position[1]))
        return (best_position[0], best_position[1])
    
def game_loop(gridPlay)->tuple:
    last_play: Range = Range(0, 0, 2)
    while True:
        
        # Player play turn
        position: list = askPosition("Mettez la position sour la forme 'x:y' : ", gridPlay)
        removeFilledSlot((position[0], position[1]))
        gridPlay[position[0]][position[1]] = "x"
        last_play.set_position(position)
        
        isWon = win_check(gridPlay, 3, "x", last_play)
        print("IS WON X ? ", isWon)
        if isWon:
            printGrid(gridPlay)
            print("X a gagné la partie !!")
            return ("x",askReplay())
        
        if len(empty_slot) == 0:
            print("Egalité !")
            return ("x", askReplay())
        printGrid(gridPlay)
        # IA Play turn
        now = time()
        psoition_computer = playIA(gridPlay, 3, last_play)
        print(time()-now)
        printGrid(gridPlay)
        last_play.set_position(psoition_computer)
        isWon = win_check(gridPlay, 3, "o", last_play)
        print("IS WON O ? ", isWon)
        if isWon:
            
            print("O, a gagné")
            return ("o",askReplay())
        
        if len(empty_slot) == 0:
            print("Egalité !")
            return (" ", askReplay())
 
def init_game():
    last_winner = "o"
    player_score = 0
    computer_score = 0
    while True:
        empty_slot.clear()
        gridPlay = generateGrid()
        
        """test_exec(gridPlay, 100000)
        return"""
        
        if last_winner == "x": playIA(gridPlay, None)
        printGrid(gridPlay)
        winner, replay = game_loop(gridPlay)
        
        last_winner = winner
        if winner == "x":
            player_score += 1
        elif winner == "o":
            computer_score += 1
        printScore(player_score, computer_score)
        
        if not replay:
            print("A bientôt :)")
            exit()

"""def test_exec(grid, n):
    x = []
    y = []
    last_play: Range = Range(0, 0, 5)
    moyenne = 0
    pre_stat = time()
    for i in range(n):
        random_index, pos = getRandomGridPosition()
        popFilledSlot(random_index)
        grid[pos[0]][pos[1]] = "x"
        last_play.set_position(pos)
        now = time()
        psoition_computer = playIA(grid, last_play)
        turnTime = time() - now
        moyenne += turnTime
        last_play.set_position(psoition_computer)
        if i%1000 == 1:
            y.append(moyenne/1000)
            x.append(i)
            moyenne = 0
            
    print(f'Grid : {grid} \n Elapsed time : {time() - pre_stat} | Occurences : {n}' )
    x = np.array(x)
    y = np.array(y)
    
    X_Y_Spline = make_interp_spline(x, y)
 
    # Returns evenly spaced numbers
    # over a specified interval.
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)
    
    plt.plot(X_, Y_)  
    plt.xlabel('x - turn')
    plt.ylabel('y - time')
    plt.title('Time by turn')
    plt.show()"""

init_game()