from util.parser import Parser
from util.printer import Printer

file = open("input/3.sam", "r")
lines = [l.strip() for l in file.readlines()]

grid = Parser.parse_grid(lines, delim="")

#Printer.print_grid(grid)

def get(r,c):
    if r < 0 or r >= len(grid):
        return '.'
    if c < 0 or c >= len(grid[r]):
        return '.'
    return grid[r][c]

surroundings = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1]
]

validnumbers = []
builder = 0
valid = False
current_active_gears = []
gears = {}
for r, row in enumerate(grid):
    for c, e in enumerate(row):
        if e.isdigit():
            if builder == 0:
                builder = int(e)
                valid = False
            else:
                builder = builder * 10 + int(e)

            # check surroundings if not valid
            if not valid:
                for s in surroundings:
                    p = get(r + s[0], c + s[1])
                    if not p.isdigit() and p != ".":
                        if p == "*": # if it's a gear
                            current_active_gears.append(str(r+s[0]) + "-" + str(c+s[1]))
                        valid = True
                        break
        else:
            if valid:
                validnumbers.append(builder)
                for g in current_active_gears:
                    if g not in gears:
                        gears[g] = [builder]
                    else:
                        gears[g].append(builder)
                current_active_gears = []
            builder = 0
            valid = False

    
    # end of line > end number
    if builder > 0 and valid:
        validnumbers.append(builder)
        for g in current_active_gears:
            if g not in gears:
                gears[g] = [builder]
            else:
                gears[g].append(builder)
        current_active_gears = []
    builder = 0
    valid = False
print(sum(validnumbers))

s = sum([g[0] * g[1] for g in gears.values() if len(g) == 2])
print(s)



