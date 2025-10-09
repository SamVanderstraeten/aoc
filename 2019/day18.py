class Node:
    def __init__(self, r, c, cost):
        self.r = r
        self.c = c
        self.access = True
        self.required_keys = []

    def clear_keys(self):
        self.required_keys = []

    def coord(self):
        return (self.r, self.c)

    def __str__(self):
        return "Node (%d, %d)"%(self.r, self.c)

def parse_stuff():
    global lines, root, nodes, nav, root, keys, doors
    for r in range(len(lines)):
        for c in range(len(lines[r].strip())):
            item = lines[r][c]
            if item == "1" or item == "2" or item == "3" or item == "4":
                root = Node(r, c, 0)
                nodes.append(root)
                nav[(r,c)] = root
                root.key = item
                keys[root.coord()] = root
            elif item == ".":
                node = Node(r,c,INF)
                nodes.append(node)
                nav[(r,c)] = node
            elif item == "#":
                continue
            elif item.isupper(): # door
                node = Node(r,c,INF)
                node.access = False
                node.door = item
                nodes.append(node)
                nav[(r,c)] = node
                doors[node.coord()] = node
            else: # key 
                node = Node(r,c,INF)
                node.key = item
                nodes.append(node)
                nav[(r,c)] = node
                keys[node.coord()] = node

def get_neighbors(node):
    nbs = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if not abs(dr) + abs(dc) == 1: # no diagonal neighbors + exclude self
                continue

            nb_node = (node.r+dr, node.c+dc)
            if nb_node in nav.keys():
                #if nav[nb_node].access:
                nbs.append(nav[nb_node])
    return nbs

def cost_sort(n):
    return n.cost

def print_cost_grid():
    global lines
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            item = lines[r][c].strip()
            if (r,c) in nav:
                cost = "XX" if nav[(r,c,)].cost == INF else "%2d"%(nav[(r,c,)].cost)
                print(cost, end='')
            else:
                print(item+item, end='')
        print()

# Breadth-first search
def bfs_keys(start_node):
  next_step = [start_node]
  discovered_nodes = []
  paths = {start_node: []}
  step = 0
  result = {}

  for k in keys.keys():
      keys[k].clear_keys()

  for k in nav.keys():
      nav[k].clear_keys()
  
  while len(next_step) > 0:
    step += 1
    n_temp = []
    for visiting_node in next_step:  
        if not visiting_node in discovered_nodes:
            discovered_nodes.append(visiting_node)
            for nb in get_neighbors(visiting_node):  # add children
                nb.required_keys = visiting_node.required_keys[:]
                c = nb.coord()
                if c in keys and not keys[c].key == start_node.key and (not keys[c].key in result or result[keys[c].key][0] > step): # watch out for double access possibilities
                    result[keys[c].key] = (step, nb.required_keys)
                elif c in doors and not doors[c].door in nb.required_keys:
                    nb.required_keys.append(doors[nb.coord()].door.lower())
                n_temp.append(nb)
    next_step = n_temp

  return result

def print_keymap():
    global keymap
    for k in keymap.keys():
        print(k + " {")
        for t in keymap[k]:
            print(t + ": ", keymap[k][t])
        print("}")

def find_cheapest(currents, collection, todo, steps, store):
    global keymap
    if len(todo) == 0: # end recursion if we grabbed the last remaining key
        return steps

    st = todo[:]
    st.sort()
    tr = currents[:]
    tr.sort()
    store_key = "".join(tr) + "-" + "".join(st)
    if store_key in store:
        return steps + store[store_key]

    keyring_size = len(collection)
    cheapest = INF
    for next_key in todo:      
        required = None
        current = None
        bot_idx = -1
        for c in range(len(currents)):  
            if next_key in keymap[currents[c]]:
                current = currents[c]
                required = keymap[current][next_key][1]
                bot_idx = c

        if all(key in collection for key in required): # we can get there
            cc = currents[:]
            cc[bot_idx] = next_key
            # go get it
            nc = collection[:]
            nc.append(next_key)
            nt = todo[:]
            nt.remove(next_key)
            cost = find_cheapest(cc, nc, nt, steps+keymap[current][next_key][0], store)
            cheapest = min(cheapest, cost)
    
    store[store_key] = cheapest - steps

    return cheapest

def build_keymap():
    global keys, keymap
    for pos in keys.keys():
        node = keys[pos]
        keymap[node.key] = bfs_keys(node)

INF = 99999999
root = None
nodes = []
nav = {}
keys = {}
doors = {}
keymap = {}

#file = open("input/old/day18.txt", "r") # Part I
file = open("input/old/day18_2.txt", "r")
lines = file.readlines()

#bots = ["@"] # Part I
bots = ["1", "2", "3", "4"]

parse_stuff()
build_keymap()

allkeys = [*keymap] # list of keys (unpack)
for b in bots:
    allkeys.remove(b)

best = find_cheapest(bots, [], allkeys, 0, {})
print("Result: " + str(best))

# So, what did I do: 
# - parse the data to retrieve information about keys, doors, starting points and their respecitve locations
# - do a pre-processing step where I calculate the distance from all keys to all other (reachable) keys, together with the required keys to get there, using BFS
# - then, use recursion (find_cheapest) to find the best possible route to collect all keys with the bots
# - added a store/cache/buffer/... to the recursive function to save all previously found path sizes (e.g. current key k and keys to collect (a,b,c) = path length 25) to speed things up (drastically)
# - extend the recursive function a bit so a list of current bot states can be passed instead of just one, then added a small piece of code that selects the bot that can retrieve the next key from the todo list, selected by the algorithm