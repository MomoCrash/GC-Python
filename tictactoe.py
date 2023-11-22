WIDTH = 3
HEIGHT = 3

def generateGrid():
    return [[" "]*WIDTH]*HEIGHT
    
gridPlay = generateGrid()

def printGrid(grid):
    string = ""
    for line in grid:
        for case in line:
            string += "[" + case + "]"
        string += "\n"
    print(string)

def checkWin(grid):
    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):
            if grid[i][j] == grid[i][j+1] and grid[i][j] == grid[i][j-1] and grid[i][j]!=" ":
                return True,grid[i][j]
            elif grid[i][j] == grid[i+1][j] and grid[i][j] == grid[i-1][j] and grid[i][j]!=" ":
                return True,grid[i][j]
            elif grid[i][j] == grid[i+1][j+1] and grid[i][j] and grid[i-1][j-1]!=" ":
                return True,grid[i][j]
            else:
                return False,""

printGrid(gridPlay)
while True:
    position = input("Mettez la position sour la forme 'xy' : ")
    gridPlay[int(position[0]) - 1][int(position[1]) - 1] = "x"
    printGrid(gridPlay)
    isWon, winner=checkWin(gridPlay)
    if isWon:
        print(winner,"a gagné")
