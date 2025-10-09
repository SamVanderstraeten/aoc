from util.parser import Parser
file = open("input/9.sam", "r")
grid = Parser.parse_int_grid(file.readlines(), '')

def surround_coords(r,c):
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    return [(r+d[0],c+d[1]) for d in dir if r+d[0]>=0 and r+d[0]<len(grid) and c+d[1]>=0 and c+d[1]<len(grid[0])]

def min_surround(r, c):
    return min([grid[c[0]][c[1]] for c in surround_coords(r,c)])
    
def basin_size(r, c, closed = []):
    for s in surround_coords(r,c):
        if(grid[s[0]][s[1]] < 9 and not s in closed):
            closed.append((s[0],s[1]))
            closed = basin_size(s[0],s[1],closed)
    return closed

minima = []
for r in range(len(grid)):
    for c in range(len(grid[r])):
        n = grid[r][c]
        if n < min_surround(r,c):
            minima.append((r,c))
mins = [grid[m[0]][m[1]] for m in minima]
print("Part I: ",sum(mins) + len(mins))

sizes = []
for min in minima:
    sizes.append(len(basin_size(min[0], min[1], [min])))
sizes.sort()
print("Part II: ", sizes.pop()*sizes.pop()*sizes.pop())