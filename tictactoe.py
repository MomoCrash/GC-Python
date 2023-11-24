import random

WIDTH = 5
HEIGHT = 5

empty_slot = []

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
    
    reponse: list = input(question).split(":")
    
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
            empty_slot.append(str(i) + ":" + str(j))
            grid[i].append(" ")
            
    return grid

## Deletes slots that are already taken 
def popFilledSlot(x: int, y: int):
    
    coord_str: str = str(x) + ":" + str(y) 
    
    if coord_str in empty_slot:
        empty_slot.remove(coord_str)

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
            
            if grid[i][j] != " " and (j+1 < WIDTH and j-1 >= 0) and grid[i][j] == grid[i][j+1] and grid[i][j] == grid[i][j-1]:
                return True,grid[i][j]
            
            elif grid[i][j]!=" " and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i+1][j] and grid[i][j] == grid[i-1][j]:
                return True,grid[i][j]
            
            elif grid[i-1][j-1]!=" " and (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i+1][j+1] and grid[i][j]==grid[i-1][j-1]:
                return True,grid[i][j]
            
            elif grid[i][j]!=" " and (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i-1][j+1] and grid[i][j]==grid[i+1][j-1]:
                return True,grid[i][j]

    return False,""

# IA play logic
def getRandomGridPosition()->str:
    return random.choice(empty_slot)
    
def blockPlayer(i,j,grid,symbol):
    if grid[i][j] != " " and (j+1 < WIDTH and j-1 >= 0) and grid[i][j] == symbol and grid[i][j+1]==symbol:
        return True,i,j-1
    elif grid[i][j] != " " and (j+1 < WIDTH and j-1 >= 0) and grid[i][j] == symbol and grid[i][j-1]==symbol:
         return True,i,j+1
    elif grid[i][j]!=" " and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == symbol and grid[i+1][j]==symbol:
        return True,i-1,j
    elif grid[i][j]!=" " and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == symbol and grid[i-1][j]==symbol:
        return True,i+1,j
    elif grid[i-1][j-1]!=" " and (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == symbol and grid[i+1][j+1]==symbol:
        return True,i-1,j-1
    elif grid[i-1][j-1]!=" " and (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == symbol and grid[i-1][j-1]==symbol:
        return True,i+1,j+1
    else:
        return False,0,0
def playIA(grid):
    pos = getRandomGridPosition()
    isPlaced = False
    for i in range(HEIGHT):
        for j in range(WIDTH):
            IAWillWin,o,p=blockPlayer(i,j,grid,"o")
            playerWillWin,h,k=blockPlayer(i,j,grid,"x")
            if IAWillWin and not isPlaced:
                if grid[o][p] == " ":
                    grid[o][p]="o"
                    isPlaced= True
            elif playerWillWin and not isPlaced:
                if grid[h][k]==" ":
                    grid[h][k]="o"
                    isPlaced=True
    if not isPlaced:
        pos = getRandomGridPosition().split(":")
        popFilledSlot(pos[0], pos[1])
        grid[int(pos[0])][int(pos[1])] = "o"
    isPlaced = False
    
    
def game_loop(gridPlay)->tuple:
    while True:
        
        # Player play turn
        position: list = askPosition("Mettez la position sour la forme 'x:y' : ", gridPlay)
        popFilledSlot(position[0], position[1])
        gridPlay[position[0]][position[1]] = "x"
        isWon, winner=checkWin(gridPlay)
        if isWon:
            printGrid(gridPlay)
            print(winner, "a gagné")
            return (winner,askReplay())
        
        # IA Play turn
        playIA(gridPlay)
        printGrid(gridPlay)
        isWon, winner=checkWin(gridPlay)
        if isWon:
            
            print(winner, "a gagné")
            return (winner,askReplay())
 
def init_game():
    player_score = 0
    computer_score = 0
    empty_slot = []
    while True:
        gridPlay = generateGrid()
        
        printGrid(gridPlay)
        winner, replay = game_loop(gridPlay)
        if winner == "x":
            player_score += 1
        else:
            computer_score += 1
        printScore(player_score, computer_score)
        
        if not replay:
            print("A bientôt :)")
            exit()

init_game()