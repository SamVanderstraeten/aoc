file = open("input/day24.txt", "r")
lines = file.readlines()

grid = [line.strip() for line in lines]

def get_surrounding(grid, r, c):
    count = 0
    for s in [(-1,0),(0,-1),(0,1),(1,0)]:
        if r+s[0] >= 0 and c+s[1] >= 0 and r+s[0] < len(grid) and c+s[1] < len(grid[0]):
            if grid[r+s[0]][c+s[1]] == "#":
                count += 1
    return count

def step(grid):
    new_grid = []
    for r in range(len(grid)):
        new_grid.append([])
        for c in range(len(grid[r])):
            num = get_surrounding(grid, r, c)
            if grid[r][c] == "#" and num == 1:
                new_grid[r].append("#")
            elif grid[r][c] == "." and (num == 1 or num == 2):
                new_grid[r].append("#")
            else:
                new_grid[r].append(".")
    return new_grid

def print_grid(grid):
    for r in grid:
        for c in r:
            print(c + " ", end='')
        print()
    print()

def biodiversity(s):
    tot = 0
    for k in range(len(s)):
        tot += (2 ** k) * (1 if s[k] == "#" else 0)
    return tot

results = []
last = "--"
iter = 0
while not last in results:
    iter += 1
    results.append(last)

    grid = step(grid)
    print_grid(grid)
    last = "".join(str(item) for line in grid for item in line)

print("Part I: " + str(biodiversity(last)))



def get_surrounding_multi(grids, n, r, c):
    count = 0
    for s in [(-1,0),(0,-1),(0,1),(1,0)]:
        if r+s[0] >= 0 and c+s[1] >= 0 and r+s[0] < len(grid) and c+s[1] < len(grid[0]):
            if grid[r+s[0]][c+s[1]] == "#":
                count += 1
    return count

def step_multi(grids):
    new_grid = []
    for r in range(len(grid)):
        new_grid.append([])
        for c in range(len(grid[r])):
            num = get_surrounding(grid, r, c)
            if grid[r][c] == "#" and num == 1:
                new_grid[r].append("#")
            elif grid[r][c] == "." and (num == 1 or num == 2):
                new_grid[r].append("#")
            else:
                new_grid[r].append(".")
    return new_grid