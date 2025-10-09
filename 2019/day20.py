file = open("input/day20.txt", "r")
lines = file.readlines()

grid = []
portals = {} # {X: [(r1, c1) , (r2, c2)]}
portalmap = {} # {(r1,c1): (r2,c2)}
revportalmap = {} # {(r1,c1): X} testing purposes
portalz = {} # {(r1,c1): +1/-1} indicates which direction on z axis the portal will send you
start = target = None

def get_portal(sr, sc):
    global grid
    # Returns name, access_row and access_col for portal of which the name starts at '(sr, sc)'. Direction unknown.
    # Clears portal name characters from the grid to avoid doubles
    for d in [(0, 1, 0, -1, 0, 2), (1, 0, -1, 0, 2, 0)]:  # never right to left, so no need to check left side of character; same way, never bottom to top
        if str(grid[sr+d[0]][sc+d[1]]).isalpha():
            name = grid[sr][sc] + grid[sr+d[0]][sc+d[1]]
            if sr + d[2] < len(grid) and sc + d[3] < len(grid[0]) and grid[sr + d[2]][sc + d[3]] == 1:
                grid[sr][sc] = 0
                grid[sr + d[0]][sc + d[1]] = 0
                return name, (sr+d[2]), (sc + d[3])
            elif sr + d[4] < len(grid) and sc + d[5] < len(grid[0]) and grid[sr + d[4]][sc + d[5]] == 1:
                grid[sr][sc] = 0
                grid[sr + d[0]][sc + d[1]] = 0
                return name, (sr+d[4]), (sc + d[5])

# load grid
def load_grid():
    global grid
    for l in range(len(lines)):
        line = lines[l].rstrip('\n')
        grid.append([])
        for loc in line:
            if loc == " " or loc == "#":
                grid[l].append(0) # not accessible
            elif loc == ".":
                grid[l].append(1)
            else:
                grid[l].append(loc) 

# print grid
def print_grid():
    global grid
    for r in grid:
        for c in r:
            print(str(c) + " ", end='')
        print()

# find portals
def find_portals():
    global grid, portals, portalmap, start, target
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            o = grid[r][c]
            if str(o).isalpha():
                name, access_row, access_col = get_portal(r, c)
                if not name in portals.keys():
                    portals[name] = []
                portals[name].append((access_row, access_col))

                if not name == "AA" and not name == "ZZ":
                    if r == 0 or c == 0 or r == len(grid)-2 or c == len(grid[0])-2: # outside > go down a level (towards 0)
                        print("%s (%d, %d): -1"%(name, access_row, access_col))
                        portalz[(access_row, access_col)] = -1
                    else: # inside > go up a level
                        portalz[(access_row, access_col)] = 1


    # merge to portal map
    for name, aps in portals.items():
        if len(aps) > 1:
            portalmap[aps[0]] = aps[1]
            portalmap[aps[1]] = aps[0]
            revportalmap[aps[0]] = name
            revportalmap[aps[1]] = name
        elif name == "AA":
            start = aps[0]
        elif name == "ZZ":
            target = aps[0]

load_grid()
#print_grid()
find_portals()
#print(portals)
print(portalmap)
print(portalz)

# Breadth-first search
def bfs(start_node, end_node):
  global grid 

  next_steps = [start_node]
  discovered_nodes = []
  step = 0

  while len(next_steps) > 0:
    step += 1
    n_temp = []

    for visiting_node in next_steps:
        if visiting_node == end_node:
            return step - 1
    
        if not visiting_node in discovered_nodes:
            discovered_nodes.append(visiting_node)

            if visiting_node in portalmap and portalmap[visiting_node] not in discovered_nodes:
                n_temp.append(portalmap[visiting_node])  
            else:
                for d in [(0,1), (0, -1), (1, 0), (-1, 0)]:  # add children
                    newrow = visiting_node[0] + d[0]
                    newcol = visiting_node[1] + d[1]
                    if newrow < 0 or newrow > len(grid) or newcol < 0 or newcol > len(grid[0]):
                        continue
    
                    if grid[newrow][newcol] == 1:
                        n_temp.append((newrow, newcol))

    next_steps = n_temp

steps = bfs(start, target)
print("Part I: " + str(steps))


# Breadth-first search in 3D (recursions can count as 3rd dimension)
def bfs3d(start_node, end_node):
  global grid 

  next_steps = [start_node]
  discovered_nodes = []
  step = 0

  while len(next_steps) > 0:
    step += 1
    print("Step %d (queue size: %d)"%(step, len(next_steps)))
    n_temp = []

    for visiting_node in next_steps:
        if visiting_node == end_node:
            return step - 1

        #print("Node under investigation: " , visiting_node)
    
        if not visiting_node in discovered_nodes:
            discovered_nodes.append(visiting_node)

            teleported = False
            flat_vn = (visiting_node[0], visiting_node[1])
            if flat_vn in portalmap:
                teleport_to = (portalmap[flat_vn][0], portalmap[flat_vn][1], visiting_node[2] + portalz[flat_vn])
                if teleport_to[2] >= 0 and teleport_to[2] < 30 and not teleport_to in discovered_nodes:
                    #print("ZOOP " + revportalmap[flat_vn] + " current: ", visiting_node)
                    #print("DOWN THE RABBIT HOLE" if portalz[flat_vn] == 1 else "TOWARDS SANITY")
                    n_temp.append(teleport_to)  # switch to other level
                    teleported = True
            
            if not teleported:
                for d in [(0,1), (0, -1), (1, 0), (-1, 0)]:  # add directions
                    newrow = visiting_node[0] + d[0]
                    newcol = visiting_node[1] + d[1]
                    if newrow < 0 or newrow > len(grid) or newcol < 0 or newcol > len(grid[0]):
                        continue
    
                    if grid[newrow][newcol] == 1:
                        n_temp.append((newrow, newcol, visiting_node[2]))

    next_steps = n_temp

start = (start[0], start[1], 0)
target = (target[0], target[1], 0)
steps = bfs3d(start, target)
print("Part II: " + str(steps))