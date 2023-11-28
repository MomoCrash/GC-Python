import random
from time import *
import matplotlib.pyplot as plt

WIDTH = 3
HEIGHT = 3

empty_slot = []
deleted_element = 0

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

# Check if someone win the game
def check_lines(grid, symbol) -> tuple[bool, tuple[ list[ tuple[int, int], bool ], list[ tuple[int, int], bool ], list[ tuple[int, int], bool ] ]]:
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # Lines
            if ((j+1 < WIDTH and j-1 >= 0) and (grid[i][j+1] ==  grid[i][j-1] == symbol)) or ((j < WIDTH and j-2 >= 0) and (grid[i][j-1] ==  grid[i][j-2] == symbol)) or ((j+2 < WIDTH and j >= 0) and (grid[i][j+1] ==  grid[i][j+2] == symbol)):
                return (True, (i, j))
            
            # Column
            elif ((i+1 < HEIGHT and i-1 >= 0) and (grid[i+1][j] == grid[i-1][j] == symbol)) or ((i < HEIGHT and i-2 >= 0) and (grid[i-1][j] == grid[i-2][j] == symbol)) or ((i+2 < HEIGHT and i >= 0) and (grid[i+1][j] == grid[i+2][j] == symbol)):
                return (True, (i, j))
            
            # Right Diagonal
            elif ((j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and (grid[i+1][j+1] == grid[i-1][j-1] == symbol)) or ((j+2 < WIDTH and j >= 0) and (i+2 < HEIGHT and i >= 0) and (grid[i+1][j+1] == grid[i+2][j+2] == symbol)) or ((j < WIDTH and j-2 >= 0) and (i < HEIGHT and i-2 >= 0) and (grid[i-1][j-1] == grid[i-2][j-2] == symbol)):
                return (True, (i, j))
            
            # Left Diagonal
            elif ((j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and (grid[i-1][j+1] == grid[i+1][j-1] == symbol)) or ((j+2 < WIDTH and j >= 0) and (i < HEIGHT and i-2 >= 0) and (grid[i-1][j+1] == grid[i-2][j+2] == symbol)) or ((j < WIDTH and j-2 >= 0) and (i+2 < HEIGHT and i >= 0) and (grid[i+1][j-1] == grid[i+2][j-2] == symbol)):
                return (True, (i, j))
            
    return (False, (0,0))

# IA play logic
def getRandomGridPosition()->tuple:
    random_index: int = random.randint(0, len(empty_slot)-1)
    return (random_index, empty_slot[random_index])
    
def playIA(grid):
    
    isPlaced = False
    best_x, best_y = 0,0
    
    ia_line_info = check_lines(grid, "o")
    if ia_line_info[0]:
        best_x, best_y = ia_line_info[1][0], ia_line_info[1][1]
        isPlaced = True
    else:
        ia_line_info = check_lines(grid, "x")
        if ia_line_info[0]:
            best_x, best_y = ia_line_info[1][0], ia_line_info[1][1]
            isPlaced = True
    
    if not isPlaced or grid[best_x][best_y] != " ":
        random_index, pos = getRandomGridPosition()
        popFilledSlot(random_index)
        grid[int(pos[0])][int(pos[1])] = "o"
        
    elif grid[best_x][best_y] == " ":
        grid[best_x][best_y]="o"
        removeFilledSlot((best_x, best_y))
    
    isPlaced = False
    
def game_loop(gridPlay)->tuple:
    while True:
        
        # Player play turn
        position: list = askPosition("Mettez la position sour la forme 'x:y' : ", gridPlay)
        removeFilledSlot((position[0], position[1]))
        gridPlay[position[0]][position[1]] = "x"
        isWon = check_lines(gridPlay, "x")
        if isWon[0] and gridPlay[isWon[1][0]][isWon[1][1]] == "x":
            printGrid(gridPlay)
            print("X a gagné la partie !!")
            return ("x",askReplay())
        
        if len(empty_slot) == 0:
            print("Egalité !")
            return ("x", askReplay())
        
        # IA Play turn
        now = time()
        playIA(gridPlay)
        print(time()-now)
        printGrid(gridPlay)
        isWon = check_lines(gridPlay, "o")
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
        
        #test_exec(gridPlay, 10000)
        #return
        
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
    for i in range(n):
        random_index, pos = getRandomGridPosition()
        popFilledSlot(random_index)
        grid[pos[0]][pos[1]] = "x"
        now = time()
        playIA(grid)
        turnTime = time() - now
        if i%100 == 1:
            y.append(turnTime)
            x.append(i)
        print(i)
    
    plt.plot(x, y)  
    plt.xlabel('x - turn')
    plt.ylabel('y - time')
    plt.title('Time by turn')
    plt.show()

init_game()