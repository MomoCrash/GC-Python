import random

WIDTH = 5
HEIGHT = 5

def askPosition(question):
    input(question)

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
