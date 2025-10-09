import math

file = open("input/day10demo.txt", "r")
lines = file.readlines()


grid = [[1 if x == "#" else 0 for x in line] for line in lines]

def scan_asteroids(grid, r, c):
    asteroid_map = {}
    full = []
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            item = grid[row][col]
            if item == 0:
                continue
            if row == r and col == c:
                continue

            dist = math.sqrt((row - r ) ** 2 + (col - c) ** 2)
            dir = (round((row - r) / dist, 4), round((col - c) / dist, 4)) # normalized direction

            if not dir in asteroid_map:
                asteroid_map[dir] = []

            asteroid_map[dir].append((dist, row, col))

    return asteroid_map

max_num_asteroids = 0
base_map = None
for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if grid[row][col] == 0:
            continue

        ast_map = scan_asteroids(grid, row, col)
        if len(ast_map.keys()) > max_num_asteroids:
            max_num_asteroids = len(ast_map.keys())
            base_map = ast_map

print("Viewable asteroids on best location: " + str(max_num_asteroids))

# Part II
directions = base_map.keys()

# sort directions
full_sorted = []
q1 = []
q2 = []
q3 = []
q4 = []
for dir in directions:
    if dir[0] < 0 and dir[1] >=0:
        q1.append(dir)
    elif dir[0] >= 0 and dir[1] > 0:
        q2.append(dir)
    elif dir[0] > 0 and dir[1] <= 0:
        q3.append(dir)
    elif dir[0] <= 0 and dir[1] < 0:
        q4.append(dir)

q1.sort(key=lambda tup: tup[1])  # sorts in place on x
q2.sort(key=lambda tup: tup[1], reverse = True)  # sorts in place on x
q3.sort(key=lambda tup: tup[1], reverse = True)
q4.sort(key=lambda tup: tup[1])

full_sorted = q1 + q2 + q3 + q4

count = 0
dir_idx = 0
while count < 200:
    next_dir = full_sorted[dir_idx]
    base_map[next_dir].sort(key=lambda tup: tup[0])
    popped = base_map[next_dir].pop(0)    
    count += 1
    print("Obliterated asteroid #%d on (r: %d, c: %d) => '%d'" %(count, popped[1], popped[2], (popped[2]*100+popped[1])))

    dir_idx = (dir_idx + 1)%len(full_sorted)
    while len(base_map[full_sorted[dir_idx]]) == 0:
        dir_idx = (dir_idx + 1)%len(full_sorted)   
    