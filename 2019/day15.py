from stepmachine import Machine
from enum import Enum

file = open("input/day15.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]

class Move(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

rev_move = {1: 2, 2: 1, 3:4, 4: 3}
move_coord = {1: (-1,0), 2: (1,0), 3: (0, 1), 4: (0, -1)}

class Result(Enum):
    WALL = 0
    MOVED = 1
    OXYGEN_SYSTEM = 2

search_radius = 100
grid = [[0 for i in range(search_radius)] for j in range(search_radius)]

# Breadth-first search
def bfs(machine:Machine, start_node):
  global grid 
  queue = [start_node]
  discovered_nodes = []
  paths = {start_node: []}

  max_len = 0

  while len(queue) > 0:
    visiting_node = queue.pop(0) # pop first node
    print("I'm in " + str(visiting_node))
    
    if not visiting_node in discovered_nodes:
      for m in paths[visiting_node]: # get back there
        machine.add_input(m.value)
        o = machine.run()

      discovered_nodes.append(visiting_node)
      for move in Move:  # add children
        machine.add_input(move.value)
        result = machine.run()

        # Part I
        #if result == Result.OXYGEN_SYSTEM.value: # FOUND
            #print("FOUND!")
            #print(str(paths[visiting_node]))
            #print(len(paths[visiting_node]))
            # 411 too low
            #return
        #elif not result == Result.WALL.value:

        # Part II, keep searching
        if not result == Result.WALL.value:
            #print("OK")
            m = move_coord[move.value]
            n = (visiting_node[0]+m[0], visiting_node[1]+m[1])
            paths[n] = paths[visiting_node][:]
            paths[n].append(move)
            queue.append(n)

            grid[n[0]][n[1]] = 1

            max_len = max(max_len, len(paths[n]))

            #print("BACK UP")
            machine.add_input(rev_move[move.value])
            machine.run()

    for m in reversed(paths[visiting_node]): # get back there
        machine.add_input(rev_move[m.value])
        o = machine.run()

  print("MAX LENGTH: " + str(max_len))

repair_bot = Machine("Bot", fields, [])

cx = cy = search_radius // 2
grid[cx][cy] = 1  

start_node = (cx, cy)
bfs(repair_bot, start_node)

for r in grid:
    for item in r:
        print("#" if item == 0 else ".", end='')
    print()