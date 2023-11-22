WIN_COMBI = [((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2))]
gridPlay = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]

def updateGrid(grid):
     return f'[{grid[0][0]}] | [{grid[0][1]}] | [{grid[0][2]}] \n---------------- \n[{grid[1][0]}] | [{grid[1][1]}] | [{grid[1][2]}] \n--------------- \n[{grid[2][0]}] | [{grid[2][1]}] | [{grid[2][2]}]'

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

print(updateGrid(gridPlay))
while True:
    position = input("Mettez la position sour la forme 'xy' : ")
    gridPlay[int(position[0]) - 1][int(position[1]) - 1] = "x"
    print(updateGrid(gridPlay))
    isWon, winner=checkWin(gridPlay)
    if isWon:
        print(winner,"a gagné")