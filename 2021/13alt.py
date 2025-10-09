from util.printer import Printer
import numpy as np
file = open("input/13.sam", "r")
lines = file.readlines()
# Alternative solution to day 13 as numpy exercise
width = max([int(l.strip().split(",")[0]) if len(l.strip().split(","))>1 else -1 for l in lines])+1
height = max([int(l.strip().split(",")[1]) if len(l.strip().split(","))>1 else -1 for l in lines])+1
grid = np.zeros((height,width), np.int32)
initializing = True
for line in lines:
    if initializing:
        if line.strip() == "":
            initializing = False
            continue
        x,y = tuple(map(int, line.strip().split(",")))
        grid[y][x] = 1
    else:
        f = line.strip().split(" ")[-1].split("=")
        height = len(grid)
        width = len(grid[0])
        if f[0] == "x":
            np.c_[grid, np.zeros((height, (2*int(f[1])+1)-width))]
            add = np.fliplr(grid[:,int(f[1])+1:])
            base = grid[:,:int(f[1])]
            grid = base + add
        elif f[0] == "y":
            np.r_[grid, np.zeros(((2*int(f[1])+1)-height, width))]
            add = np.flipud(grid[int(f[1])+1:,:])
            base = grid[:int(f[1]),:]
            grid = base + add
Printer.print_grid_nums(grid)