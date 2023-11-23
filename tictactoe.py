import random

WIDTH = 5
HEIGHT = 5

## Ask grid position 
def askPosition(question, grid):
    reponse = input(question).split(":")
    formated = False
    while not formated:
        try:
            x = int(reponse[0])
            y = int(reponse[1])
            if (x > 0 and x <= WIDTH) and (y > 0 and y <= HEIGHT):
                if (grid[x-1][y-1] == " "):
                    return (x-1, y-1)
                else:
                    print("Quelqu'un a déjà joué ici !")
                    reponse = input(question).split(":")
            else:
                print("Votre placement est hors des limites de la grille !")
                reponse = input(question).split(":")
        except:
            print("Votre position n'existe pas essayez par exemple : 1:1.")
            reponse = input(question).split(":")
    


## Grid generation
def generateGrid():
    grid = []
    for i in range(HEIGHT):
        grid.append([])
        for j in range(WIDTH):
            grid[i].append(" ")
    return grid

## Print grid to console
def printGrid(grid):
    string = ""
    for line in grid:
        for case in line:
            string += "[" + case + "]"
        string += "\n"
    print(string)

# Check if someone win the game
def checkWin(grid):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] != " " and (j+1 < WIDTH and j-1 >= 0) and grid[i][j] == grid[i][j+1] and grid[i][j] == grid[i][j-1]:
                return True,grid[i][j]
            elif grid[i][j]!=" " and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i+1][j] and grid[i][j] == grid[i-1][j]:
                return True,grid[i][j]
            elif grid[i-1][j-1]!=" " and (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i+1][j+1] and grid[i][j]==grid[i-1][j-1]:
                return True,grid[i][j]

    return False,""

# IA play logic
def getRandomGridPosition():
    return (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))

def getPlayAtPos(pos, grid):
    return grid[pos[0]][pos[1]] == " "

def playIA(grid):
    pos = getRandomGridPosition()
    while not getPlayAtPos(pos, grid):
        pos = getRandomGridPosition()
    grid[pos[0]][pos[1]] = "o"
    
gridPlay = generateGrid()
printGrid(gridPlay)
replay:bool = True

while replay:
    position = askPosition("Mettez la position sour la forme 'x:y' : ", gridPlay)
    gridPlay[position[0]][position[1]] = "x"
    
    isWon, winner=checkWin(gridPlay)
    if isWon:
        printGrid(gridPlay)
        print(winner,"a gagné")
        replay= input("Voulez-vous rejouer ? y/n ") == "y"
        gridPlay = generateGrid()
    
    playIA(gridPlay)
    printGrid(gridPlay)
    isWon, winner=checkWin(gridPlay)
    
    if isWon:
        print(winner,"a gagné")
        replay= input("Voulez-vous rejouer ? y/n ") == "y"
        gridPlay = generateGrid()