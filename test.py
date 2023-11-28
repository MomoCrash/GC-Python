# Check if someone win the game
def check_lines(grid, symbol) -> tuple[bool, tuple[ list[ tuple[int, int], bool ], list[ tuple[int, int], bool ], list[ tuple[int, int], bool ] ]]:
    for i in range(HEIGHT):
        for j in range(WIDTH):
            
            # Lines
            if (j+1 < WIDTH and j-1 >= 0) and (grid[i][j] == grid[i][j+1] ==  grid[i][j-1] == symbol):
                return (True, (i, j))
            
            # Column
            elif (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i+1][j] == grid[i-1][j] == symbol:
                return (True, (i, j))
            
            # Right Diagonal
            elif (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i+1][j+1] == grid[i-1][j-1] == symbol:
                return (True, (i, j))
            
            # Left Diagonal
            elif (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0) and grid[i][j] == grid[i-1][j+1] == grid[i+1][j-1] == symbol:
                return (True, (i, j))
            
            # Lines
            elif (j+1 < WIDTH and j-1 >= 0):
                return ( False, ( [(i,j+1), grid[i][j+1] == symbol], [(i,j), grid[i][j] == symbol],  [(i,j-1), grid[i][j-1] == symbol] ) )
            # Column
            elif (i+1 < HEIGHT and i-1 >= 0):
                return ( False, ( [(i+1,j), grid[i+1][j] == symbol], [(i,j), grid[i][j] == symbol],  [(i-1,j), grid[i-1][j] == symbol] ) )
            # Right Diagonal
            elif (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0):
                return ( False, ( [(i-1,j-1), grid[i-1][j-1] == symbol], [(i,j), grid[i][j] == symbol],  [(i+1,j+1), grid[i+1][j+1] == symbol] ) )
            # Left Diagonal
            elif (j+1 < WIDTH and j-1 >= 0) and (i+1 < HEIGHT and i-1 >= 0):
                return ( False, ( [(i+1,j-1), grid[i+1][j-1] == symbol], [(i,j), grid[i][j] == symbol],  [(i-1,j+1), grid[i+1][j-1] == symbol] ) )
            
    return (False, (0,0))

print(True or False or False)