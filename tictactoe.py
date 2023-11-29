import random
from time import *
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

WIDTH = 1000
HEIGHT = 1000

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
        
    def in_range(self, x: int, y: int):
        if not (self.x - self.radius > x > self.x + self.radius):
            return False
        elif not (self.y - self.radius > y > self.y + self.radius):
            return False
        else:
            return True
            
    

## Print formated score
def printScore(player: int, computer: int):
    print("Score du joueur : " + str(player) + "\nScore de l'ordinateur : " + str(computer))

## Ask if player wants to replay
def askReplay()->bool:
    
    valid_anwsers = ["Y", "y", "n", "N"]
    reponse = input("Voulez-vous rejouer ? Y/n : ")
    
    while reponse not in valid_anwsers:
        reponse = input("Voulez-vous rejouer ? Y/n : ")
    
    if reponse == "Y" or reponse == "y":
        return True
    
    else:
        return False

## Ask grid position 
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
    


## Grid generation
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


## Print grid to console
def printGrid(grid):
    
    string: str = ""
    for line in grid:
        for case in line:
            string += "[" + case + "]"
        string += "\n" 
    print(string)
    

def get_inter_tiles(range: Range):
    pass


# Check if someone win the game
def check_lines(grid: list, symbol: str, check_range: Range=None) -> tuple[bool, tuple[int, int]]:
    
    if check_range is None: return (False, (0,0))
    
    min_x, max_x = check_range.min_max_x(WIDTH)
    min_y, max_y = check_range.min_max_y(HEIGHT)
    
    for i in range(min_y, max_y):
        for j in range(min_x, max_x):
            # Lines
            if ((j+1 < WIDTH and j-1 >= 0) and (grid[i][j+1] ==  grid[i][j-1] == symbol)) or ((j < WIDTH and j-2 >= 0) and (grid[i][j-1] ==  grid[i][j-2] == symbol)) or ((j+2 < WIDTH and j >= 0) and (grid[i][j+1] ==  grid[i][j+2] == symbol)):
                return (grid[i][j] == symbol, (i, j))
            
            # Column
            elif ((i+1 < HEIGHT and i-1 >= 0) and (grid[i+1][j] == grid[i-1][j] == symbol)) or ((i < HEIGHT and i-2 >= 0) and (grid[i-1][j] == grid[i-2][j] == symbol)) or ((i+2 < HEIGHT and i >= 0) and (grid[i+1][j] == grid[i+2][j] == symbol)):
                return (grid[i][j] == symbol, (i, j))
            
            # Right Diagonal
            elif ((j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and (grid[i+1][j+1] == grid[i-1][j-1] == symbol)) or ((j+2 < WIDTH and j >= 0) and (i+2 < HEIGHT and i >= 0) and (grid[i+1][j+1] == grid[i+2][j+2] == symbol)) or ((j < WIDTH and j-2 >= 0) and (i < HEIGHT and i-2 >= 0) and (grid[i-1][j-1] == grid[i-2][j-2] == symbol)):
                return (grid[i][j] == symbol, (i, j))
            
            # Left Diagonal
            elif ((j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and (grid[i-1][j+1] == grid[i+1][j-1] == symbol)) or ((j+2 < WIDTH and j >= 0) and (i < HEIGHT and i-2 >= 0) and (grid[i-1][j+1] == grid[i-2][j+2] == symbol)) or ((j < WIDTH and j-2 >= 0) and (i+2 < HEIGHT and i >= 0) and (grid[i+1][j-1] == grid[i+2][j-2] == symbol)):
                return (grid[i][j] == symbol, (i, j))
            
    return (False, (0,0))

# IA play logic
def getRandomGridPosition()->tuple:
    random_index: int = random.randint(0, len(empty_slot)-1)
    return (random_index, empty_slot[random_index])
    
def playIA(grid: list, last_range: Range) -> tuple[int, int]:
    
    isPlaced: bool = False
    best_x, best_y = (0,0)
    
    ia_line_info = check_lines(grid, "o", last_range)
    if ia_line_info[0]:
        best_x, best_y = ia_line_info[1][0], ia_line_info[1][1]
        isPlaced = True
    else:
        ia_line_info = check_lines(grid, "x", last_range)
        if ia_line_info[0]:
            best_x, best_y = ia_line_info[1][0], ia_line_info[1][1]
            isPlaced = True
    
    if not isPlaced or grid[best_x][best_y] != " ":
        random_index, pos = getRandomGridPosition()
        popFilledSlot(random_index)
        grid[pos[0]][pos[1]] = "o"
        return pos
        
    else:
        grid[best_x][best_y]="o"
        removeFilledSlot((best_x, best_y))
        return (best_x, best_y)
    
def game_loop(gridPlay)->tuple:
    last_play: Range = Range(0, 0, 2)
    while True:
        
        # Player play turn
        position: list = askPosition("Mettez la position sour la forme 'x:y' : ", gridPlay)
        removeFilledSlot((position[0], position[1]))
        gridPlay[position[0]][position[1]] = "x"
        last_play.set_position(position)
        
        isWon = check_lines(gridPlay, "x", last_play, True)
        if isWon[0] and gridPlay[isWon[1][0]][isWon[1][1]] == "x":
            printGrid(gridPlay)
            print("X a gagné la partie !!")
            return ("x",askReplay())
        
        if len(empty_slot) == 0:
            print("Egalité !")
            return ("x", askReplay())
        
        # IA Play turn
        now = time()
        psoition_computer = playIA(gridPlay, last_play)
        print(time()-now)
        printGrid(gridPlay)
        last_play.set_position(psoition_computer)
        isWon = check_lines(gridPlay, "o", last_play, True)
        if isWon[0] and gridPlay[isWon[1][0]][isWon[1][1]] == "o":
            
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
        
        test_exec(gridPlay, 100000)
        return
        
        if last_winner == "x": playIA(gridPlay)
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

def test_exec(grid, n):
    x = []
    y = []
    last_play: Range = Range(0, 0, 5)
    moyenne = 0
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
    plt.show()

init_game()