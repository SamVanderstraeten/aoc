file = open("input/17.sam", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

CYCLES = 6
active = {}

# Initialize active cells from file
for (row, line) in enumerate(lines):
    for (col, cell) in enumerate(line):
        if cell == "#":
            active[(row, col, 0, 0)] = "#"

def get_neighbors(cube):
    nbs = []
    for y in [-1,0,1]:
        for x in [-1,0,1]:
            for z in [-1,0,1]:
                for w in [-1,0,1]:
                    if x==y==z==w==0:
                        continue
                    else:
                        nbs.append((cube[0]+y, cube[1]+x, cube[2]+z, cube[3]+w))
    return nbs

def get_active_neighbors(cube,active):
    count = 0
    for y in [-1,0,1]:
        for x in [-1,0,1]:
            for z in [-1,0,1]:
                for w in [-1,0,1]:
                    if x != 0 or y != 0 or z != 0 or w != 0:
                        if (cube[0]+y,cube[1]+x,cube[2]+z,cube[3]+w) in active:
                            count += 1
    return count

for i in range(1, CYCLES+1):
    print("Cycle: ", i)
    
    cubeset = set()
    for active_cube in active:
        for nb in get_neighbors(active_cube):
            cubeset.add(nb)

    newactive = {}
    for cube in cubeset:
        ns = get_active_neighbors(cube,active)
        if ns < 2 or ns > 3:
            continue
        if cube in active and (ns == 2 or ns == 3):
            newactive[cube] = "#"
        elif (not cube in active) and ns == 3:
            newactive[cube] = "#"
    active = newactive

print(">>",len(active.keys()))