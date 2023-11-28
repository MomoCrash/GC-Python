import random

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
        input("Voulez-vous rejouer ? Y/n : ")
    
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
    global deleted_element
    print("index : ",index)
    empty_slot[index-deleted_element]=empty_slot[-1]
    empty_slot.pop()
    deleted_element += 1

## Print grid to console
def printGrid(grid):
    
    string: str = ""
    for line in grid:
        for case in line:
            string += "[" + case + "]"
        string += "\n" 
    print(string)

# Check if someone win the game
def checkWin(grid) -> bool:
    for i in range(HEIGHT):
        for j in range(WIDTH):
            
            # Lines
            if grid[i][j] != " " and (j+1 < WIDTH and j-1 >= 0) and grid[i][j] == grid[i][j+1] and grid[i][j] == grid[i][j-1]:
                return True,grid[i][j]
            
            # Column
            elif grid[i][j]!=" " and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i+1][j] and grid[i][j] == grid[i-1][j]:
                return True,grid[i][j]
            
            # Right Diagonal
            elif grid[i][j]!=" " and (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i+1][j+1] and grid[i][j]==grid[i-1][j-1]:
                return True,grid[i][j]
            
            # Left Diagonal
            elif grid[i][j]!=" " and (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i-1][j+1] and grid[i][j]==grid[i+1][j-1]:
                return True,grid[i][j]

    return False,""

# IA play logic
def getRandomGridPosition()->tuple:
    return random.choice(empty_slot)
    
def blockPlayer(i,j,grid,symbol):
    
    #line
    if grid[i][j] != " " and (j+1 < WIDTH and j >= 0) and grid[i][j] == symbol and grid[i][j+1]==symbol:
        return True,i,j-1
    elif grid[i][j] != " " and (j < WIDTH and j-1 >= 0) and grid[i][j] == symbol and grid[i][j-1]==symbol:
         return True,i,j+1
    elif grid[i][j] != " " and (j+2 < WIDTH and j >= 0) and grid[i][j] == symbol and grid[i][j+2]==symbol:
        return True,i,j+1
     
    #column 
    elif grid[i][j]!=" " and (i+1 < HEIGHT and i >= 0) and grid[i][j] == symbol and grid[i+1][j]==symbol:
        return True,i-1,j
    elif grid[i][j]!=" " and (i < HEIGHT and i-1 >= 0) and grid[i][j] == symbol and grid[i-1][j]==symbol:
        return True,i+1,j
    elif grid[i][j]!=" " and (i+2 < HEIGHT and i >= 0) and grid[i][j] == symbol and grid[i+2][j]==symbol:
        return True,i+1,j
    
    #diagonal right
    elif grid[i][j]!=" " and (j+1 < WIDTH and j >= 0) and (i+1 < HEIGHT and i >= 0) and grid[i][j] == symbol and grid[i+1][j+1]==symbol:
        return True,i-1,j-1
    elif grid[i][j]!=" " and (j < WIDTH and j-1 >= 0) and (i < HEIGHT and i-1 >= 0) and grid[i][j] == symbol and grid[i-1][j-1]==symbol:
        return True,i+1,j+1
    elif grid[i][j]!=" " and (j+2 < WIDTH and j >= 0) and (i+2 < HEIGHT and i >= 0) and grid[i][j] == symbol and grid[i+2][j+2]==symbol:
        return True,i+1,j+1
    
    #diagonal left
    elif grid[i][j]!=" " and (j < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i >= 0) and grid[i][j] == symbol and grid[i+1][j-1] == symbol:
        return True,i-1,j+1
    elif grid[i][j]!=" " and (j+1 < WIDTH and j >= 0) and (i < HEIGHT and i-1 >= 0) and grid[i][j] == symbol and grid[i-1][j+1] == symbol:
        return True,i+1,j-1
    elif grid[i][j]!=" " and (j < WIDTH and j-2 >= 0) and (i+2 < HEIGHT and i >= 0) and grid[i][j] == symbol and grid[i+2][j-2] == symbol:
        return True,i+1,j-1
    
    #si y'a r
    else:
        return False,0,0
    
def playIA(grid):
    
    pos = getRandomGridPosition()
    IAWin = False
    isPlaced = False
    best_x, best_y = 0,0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            IAWillWin,o,p=blockPlayer(i,j,grid,"o")
            if IAWillWin:
                best_x, best_y = o, p
                isPlaced = True
            elif not IAWin:
                IABlockPlayer,h,k=blockPlayer(i,j,grid,"x")
                if IABlockPlayer:
                    best_x, best_y = h, k
                    isPlaced = True
    
    print(best_x, best_y)
    print(empty_slot)
    if not isPlaced or grid[best_x][best_y] != " ":
        print("RANDOM")
        pos = getRandomGridPosition()
        print(pos)
        popFilledSlot(pos[0]+WIDTH*pos[1])
        grid[int(pos[0])][int(pos[1])] = "o"
        
    elif grid[best_x][best_y] == " ":
        grid[best_x][best_y]="o"
        popFilledSlot(best_y+WIDTH*best_x)
    
    isPlaced = False
    
def game_loop(gridPlay)->tuple:
    while True:
        
        # Player play turn
        position: list = askPosition("Mettez la position sour la forme 'x:y' : ", gridPlay)
        popFilledSlot(position[1]+WIDTH*position[0])
        gridPlay[position[0]][position[1]] = "x"
        isWon, winner=checkWin(gridPlay)
        if isWon:
            printGrid(gridPlay)
            print(winner, "a gagné")
            return (winner,askReplay())
        
        if len(empty_slot) == 0:
            print("Egalité !")
            return ("x", askReplay())
        
        # IA Play turn
        playIA(gridPlay)
        printGrid(gridPlay)
        isWon, winner=checkWin(gridPlay)
        if isWon:
            
            print(winner, "a gagné")
            return (winner,askReplay())
        
        if len(empty_slot) == 0:
            print("Egalité !")
            return ("o", askReplay())
 
def init_game():
    last_winner = "o"
    player_score = 0
    computer_score = 0
    while True:
        empty_slot.clear()
        gridPlay = generateGrid()
        
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

init_game()