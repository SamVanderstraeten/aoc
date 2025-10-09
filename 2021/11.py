from util.parser import Parser
file = open("input/11.sam", "r")
grid = Parser.parse_int_grid(file.readlines(),'')
PULSE_POWER = 10
flash = 0
def increase(r,c):
    global grid, flash_octopus
    grid[r][c] += 1
    if grid[r][c] == PULSE_POWER:
        flash_octopus(r,c)

def flash_octopus(r,c):
    global flash
    flash += 1
    for i in range(-1,2):
        for j in range(-1,2):
            if (i!=0 or j!=0) and r+i in range(0,len(grid)) and c+j in range(0, len(grid[0])):
                increase(r+i,c+j)

for i in range(10000):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            increase(r,c)  

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] >= PULSE_POWER:
                grid[r][c] = 0
                count += 1

    if i == 99:
        print("Part I",flash) 
    if count == 100:
        print("Part II",str(i+1))
        break