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
        
printGrid(gridPlay)