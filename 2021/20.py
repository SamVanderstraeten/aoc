import numpy as np
from util.parser import Parser
file = open("input/20.sam", "r")
lines = file.readlines()
algo = lines[0].strip()
img = np.array(Parser.parse_grid(lines[2:],"",{'#':1,'.':0}))

def pad_grid(grid, s=0, n=3):
    size = (len(grid)+n*2,len(grid[0])+n*2)
    g = np.zeros(size, dtype=int) if s==0 else np.ones(size,dtype=int)
    g[n:n+len(grid),n:n+len(grid[0])] = grid
    return g

def run_algo(img, algo):
    enhanced = img.copy()
    for i in range(1,len(img)-1):
        for j in range(1,len(img[i])-1):
            bin = ''.join([str(x) for x in img[i-1:i+2,j-1:j+2].flatten()])
            enhanced[i,j] = 1 if algo[int(bin,2)] == "#" else 0
    return enhanced[1:-1,1:-1]

for i in range(50):
    if i==2: print("Part I",sum(sum(img)))
    img = pad_grid(img, i%2) # index 0 = "#" and index 1 = "." >> infinite space alternates between #(1) and .(0) every other iteration
    img = run_algo(img, algo)
print("Part II",sum(sum(img)))