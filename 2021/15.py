from util.parser import Parser 
import numpy as np
file = open("input/15.sam", "r")
grid = Parser.parse_int_grid(file.readlines(),'')

def nbs(v):
    return [(v[0]+a[0],v[1]+a[1]) for a in [(-1,0),(1,0),(0,-1),(0,1)] if v[0]+a[0] >= 0 and v[1]+a[1] >= 0 and v[0]+a[0] < len(grid[0]) and v[1]+a[1] < len(grid)]

def h(v,t):
    return (abs(t[0]-v[0])+abs(t[1]-v[1])) * 1

def a(v, target):
    queue = {v:0}
    visited = {}
    while (len(queue) > 0):
        v = min(queue, key=queue.get)
        cost = queue[v]
        cost = 0 if cost == 0 else cost - h(v,target)
        del queue[v]       

        for nb in nbs(v):
            if nb == target:
                return cost+ grid[nb[0]][nb[1]]
            nb_cost = cost + grid[nb[0]][nb[1]] + h(nb,target)
        
            if nb in queue.keys() and queue[nb] < nb_cost:
                continue
            if nb in visited.keys() and visited[nb] < nb_cost:
                continue
            queue[nb] = nb_cost
        visited[v] = cost
    return -1

p = a((0,0), (len(grid[0])-1, len(grid)-1))
print("Part I:",p)

# Extend grid in x direction
grid = np.array(grid)
nextgrid = grid.copy()
for x in range(4):
    nextgrid = (nextgrid%9)+1
    grid = np.append(grid, nextgrid, 1)
# Extend grid in y direction
nextgrid = grid.copy()
for y in range(4):
    nextgrid = (nextgrid%9)+1
    grid = np.append(grid, nextgrid, 0)
    
p = a((0,0), (len(grid[0])-1, len(grid)-1))
print("Part II:",p)