from util.printer import Printer
file = open("input/13.sam", "r")
lines = file.readlines()

grid = {}
folds = []
height = -1
width = -1
for line in lines:
    if line.strip() == "":
        continue
    f = line.strip().split(" ")
    if len(f) > 2:
        folds.append(f[-1].split("="))
    else:
        x,y = tuple(map(int, line.strip().split(",")))
        width = max(width, x)
        height = max(height, y)
        if x in grid.keys():
            grid[x][y] = 1
        else:
            grid[x] = {y: 1}

for c, fold in enumerate(folds):
    if fold[0] == "y":
        for x in grid.keys():
            n = {}
            for y in grid[x]:
                if y >= int(fold[1]):
                    transfer = height-y
                    n[transfer] = 1
                else:
                    n[y] = 1
            grid[x] = n
        height = int(fold[1])-1
    elif fold[0] == "x":
        for i in range(int(fold[1]), width+1):
            if i in grid.keys():
                transfer = width-i
                if i in grid.keys():
                    if transfer in grid.keys():
                        for l in grid[i]:
                            grid[transfer][l] = 1
                    else:
                        grid[transfer] = grid[i]
                grid.pop(i, None)
        width = int(fold[1])-1
    
    if c == 0:
        num = sum([len(grid[x]) for x in grid.keys()])
        print("Part I",num)

pr = [['.' for x in range(width+1)] for y in range(height+1)]
for x in grid:
    for y in grid[x]:
        pr[y][x] = "#"
Printer.print_grid(pr)