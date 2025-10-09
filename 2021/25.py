import copy
from util.parser import Parser
file = open("input/25.sam", "r")
lines = file.readlines()
grid = Parser.parse_grid(lines,'')
EMPTY = '.'

def cucumber_dance(grid):
    grid_state = copy.deepcopy(grid)
    count = 0
    for r,row in enumerate(grid_state):
        for c,el in enumerate(row):
            if el == '>':
                next_c = (c+1)%len(row)
                if grid_state[r][next_c] == EMPTY:
                    grid[r][c] = EMPTY
                    grid[r][next_c] = el
                    count+=1
    grid_state = copy.deepcopy(grid)
    for r,row in enumerate(grid_state):
        for c,el in enumerate(row):
            if el == 'v':
                next_r = (r+1)%len(grid)
                if grid_state[next_r][c] == EMPTY:
                    grid[r][c] = EMPTY
                    grid[next_r][c] = el
                    count+=1
    return grid, count

moves = 99
rounds = 0
while moves > 0:
    rounds += 1
    grid,moves = cucumber_dance(grid)
print(rounds)
