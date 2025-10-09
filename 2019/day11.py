from stepmachine import Machine

file = open("input/day11.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]

machine = Machine("Painter", fields, [])

# part I : grid = {}
# part II :
grid = {"0-0": 1}

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_dir = 0
current_row = 0
current_col = 0

while not machine.halted:
    input = 0
    current_pos = str(current_row) + "-" + str(current_col)
    if current_pos in grid:
        input = grid[current_pos]
        
    machine.add_input(input)
    color = machine.run()
    turn = machine.run()

    grid[current_pos] = color
    current_dir += (1 if turn == 1 else -1)
    current_dir = (current_dir + len(directions)) % len(directions)
    current_row += directions[current_dir][0]
    current_col += directions[current_dir][1]

print(len(grid.keys()))

min_x = 9999
min_y = 9999
max_x = -9999
max_y = -9999
for k in grid.keys():
    pos = k.split("-")
    pos[0] = int(pos[0])
    pos[1] = int(pos[1])
    min_x = min(min_x, pos[1])
    max_x = max(max_x, pos[1])
    min_y = min(min_y, pos[0])
    max_y = max(max_y, pos[0])

for r in range(0, abs(max_y-min_y+1)):
    for c in range(0, abs(max_x-min_x+1)):
        pos = str(min_y+r) + "-" + str(min_x+c)
        if pos in grid.keys() and grid[pos] == 1:
            print("# ", end='')
        else:
            print("  ", end='')
    print()