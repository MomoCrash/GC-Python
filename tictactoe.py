WIN_COMBI = [((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2))]
gridPlay = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]

def updateGrid(grid):
     return f'[{grid[0][0]}] | [{grid[0][1]}] | [{grid[0][2]}] \n---------------- \n[{grid[1][0]}] | [{grid[1][1]}] | [{grid[1][2]}] \n--------------- \n[{grid[2][0]}] | [{grid[2][1]}] | [{grid[2][2]}]'

def checkCombinaison(symbol, grid):
    for c in WIN_COMBI:
        currentWin = True
        for pos in c:
            if grid[pos[0]][pos[1]] != symbol and currentWin == True:
                currentWin = False
        if currentWin:
            return True
    return False

print(updateGrid(gridPlay))
while True:
    position = input("Mettez la position sour la forme 'xy' : ")
    gridPlay[int(position[0]) - 1][int(position[1]) - 1] = "x"
    print(updateGrid(gridPlay))
    print(checkCombinaison("x", gridPlay))