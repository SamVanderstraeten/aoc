import re 

file = open("input/5.sam", "r")
data = file.readlines()
lines = [] 
for line in data:
    lines.append([int(x) for x in re.findall('\d+', line)])

cells = {}
count = 0
def hit_cell(loc):
    global count
    cells[loc] = 1 if not loc in cells else cells[loc] + 1
    if cells[loc] == 2: # only count if it reaches 2
        count += 1

for line in lines:
    if line[0]==line[2]: # vertical
        for i in range(min(line[1], line[3]), max(line[1], line[3])+1):
            hit_cell((line[0], i))
    elif line[1] == line[3]: # horizontal
        for i in range(min(line[0], line[2]), max(line[0], line[2])+1):
            hit_cell((i, line[3]))    
    else: # diagonal
        dr = 1 if line[0] < line[2] else -1
        dc = 1 if line[1] < line[3] else -1
        loc = (line[0], line[1])
        for i in range(min(line[0], line[2]), max(line[0], line[2])+1):
            hit_cell(loc)  
            loc = (loc[0]+dr,loc[1]+dc)
print(count)