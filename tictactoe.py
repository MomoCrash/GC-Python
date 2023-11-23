import random

WIDTH = 3
HEIGHT = 3


## Grid generation
def generateGrid():
    grid = []
    for i in range(HEIGHT):
        grid.append([])
        for j in range(WIDTH):
            grid[i].append(" ")
    return grid
    
gridPlay = generateGrid()

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
    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):
            if grid[i][j] == grid[i][j+1] and grid[i][j] == grid[i][j-1] and grid[i][j]!=" ":
                return True,grid[i][j]
            elif grid[i][j] == grid[i+1][j] and grid[i][j] == grid[i-1][j] and grid[i][j]!=" ":
                return True,grid[i][j]
            elif grid[i][j] == grid[i+1][j+1] and grid[i][j]==grid[i-1][j-1] and grid[i-1][j-1]!=" ":
                return True,grid[i][j]
            else:
                return False,"Bite"

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
    

printGrid(gridPlay)

while True:
    position = input("Mettez la position sour la forme 'x:y' : ")
    position = position.split(":")
    gridPlay[int(position[0]) - 1][int(position[1]) - 1] = "x"
    
    playIA(gridPlay)
    printGrid(gridPlay)
    
    isWon, winner=checkWin(gridPlay)
    if isWon:
        print(winner,"a gagné")
