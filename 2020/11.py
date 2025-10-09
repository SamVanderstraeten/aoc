from util.parser import Parser
from util.printer import Printer

file = open("input/11.sam", "r")
lines = file.readlines()

grid = Parser.parse_grid(lines, "")


def get_num_vis_occ(gridder, r, c):
    dir = [-1,0,1]
    count = 0
    for dy in dir:
        for dx in dir:
            if dx != 0 or dy != 0:
                x = 0
                y = 0
                while True:
                    x += dx
                    y += dy
                    if 0 <= c+x < len(gridder[0]) and 0 <= r+y < len(gridder):
                        if gridder[r+y][c+x] == "#":
                            count += 1
                            break
                        elif gridder[r+y][c+x] == "L":
                            break
                    else:
                        break

    return count

def get_num_adj_occ(gridder, r, c):
    dir = [-1,0,1]
    count = 0
    for y in dir:
        for x in dir:
            if x != 0 or y != 0:
                if 0 <= c+x < len(gridder[0]) and 0 <= r+y < len(gridder):
                    if gridder[r+y][c+x] == "#":
                        count += 1

    return count

def step(grid):
    newgrid = []
    for r in range(0, len(grid)):
        row = []
        for c in range(0, len(grid[0])):
            #num = get_num_adj_occ(grid, r, c) # Part 1
            num = get_num_vis_occ(grid, r, c)
            if grid[r][c] == "L" and num == 0:
                row.append("#")
            elif grid[r][c] == "#" and num >= 5: # Part 1: num >= 4
                row.append("L")
            else:
                row.append(grid[r][c])
        newgrid.append(row)
        
    return newgrid

def count_occ(grid):
    count = 0
    for row in grid:
        for seat in row:
            if seat == "#":
                count += 1
    return count

done = False
stepcount = 1
while not done:
    ng = step(grid)
    if ng == grid:
        print(stepcount)
        break
    grid = ng
    stepcount += 1
print(count_occ(grid))


        