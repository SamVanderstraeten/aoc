file = open("input/old/day3.txt", "r")
lines = file.readlines()

directions = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}
wire_a = lines[0].split(",")
wire_b = lines[1].split(",")

grid = {}

closest_cross = 1000000
fastest = 100000

counts = {"a": 0, "b": 0}

# set <id> to position <pos> in the grid
# if another id is present, we have a crossing
# keep track of closest and fastest crossing
def grid_set(pos, id):
    global closest_cross, fastest
    uid = str(pos[0]) + "-" + str(pos[1])
    counts[id] += 1

    if uid in grid.keys(): # only add if not present yet (fastest occurence counts)
        if not grid[uid][0] == id: # if different id > crossing!
            # crossing found!
            manh_dist = abs(pos[0]) + abs(pos[1])
            closest_cross = min(manh_dist, closest_cross)
            grid[uid] = (id, grid[uid][1]+counts[id], 2)
            fastest = min(fastest, grid[uid][1])
    else:
        grid[uid] = (id, counts[id], 1)

# move <amount> of steps for id <id> in direction <d>, starting from <from_pos>
def move(from_pos, d, amount, id):
    for i in range(1, amount+1):
        p = [from_pos[0] + d[0]*i, from_pos[1] + d[1]*i]
        grid_set(p, id)

    from_pos[0] += d[0] * amount
    from_pos[1] += d[1] * amount

# execute all steps in <steplist> for <id>
def steps(steplist, id):
    pos = [0, 0] # [row, col]
    st = 0
    for step in steplist:
        d = step[0]
        amount = int(step[1:])
        move(pos, directions[d], amount, id)

steps(wire_a, "a")
steps(wire_b, "b")
print("Closest: " + str(closest_cross))
print("Fastest: " + str(fastest))