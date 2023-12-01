def line_win(grid, i, j, k, symbol):
    symbol_count = 1
    for line in range(j+1, j+k):
        if j+line >= WIDTH: break
        if grid[i][line] != symbol:
            break
        else:
            symbol_count += 1
    for line in range(j-1, j-k, -1):
        if j-line < 0: break
        if grid[i][line] != symbol:
            break
        else:
            symbol_count += 1
    return symbol_count >= k

def col_win(grid, i, j, k, symbol):
    symbol_count = 1
    for col in range(i+1, i+k):
        if i+col >= HEIGHT: break
        if grid[col][j] != symbol:
            break
        else:
            symbol_count += 1
    for col in range(i-1, i-k, -1):
        if i-col < 0: break
        if grid[col][j] != symbol:
            break
        else:
            symbol_count += 1
    return symbol_count >= k

def right_diag_win(grid, i, j, k, symbol):
    symbol_count = 1
    for incre in range(1, k):
        if i+incre >= HEIGHT or j+incre >= WIDTH: break
        print(i+incre, j+incre)
        if grid[i+incre][j+incre] != symbol:
            break
        else:
            symbol_count += 1
    for decre in range(1, k):
        if i-decre < 0 or j-decre < 0: break
        if grid[i-decre][j-decre] != symbol:
            break
        else:
            symbol_count += 1
    return symbol_count >= k

def left_diag_win(grid, i, j, k, symbol):
    symbol_count = 1
    for incre in range(1, k):
        if i+incre >= HEIGHT or j+incre >= WIDTH: break
        print(i+incre, j+incre)
        if grid[i+incre][j-incre] != symbol:
            break
        else:
            symbol_count += 1
    for decre in range(1, k):
        if i-decre < 0 or j+decre >= HEIGHT: break
        if grid[i-decre][j+decre] != symbol:
            break
        else:
            symbol_count += 1
    return symbol_count >= k