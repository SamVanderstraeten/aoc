from stepmachine import Machine

file = open("input/day13.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]
fields_copy = [int(x) for x in lines[0].split(",")]

def update_grid(grid, outputs):
    ix = 0
    while ix + 2 < len(outputs):
        x = outputs[ix]
        y = outputs[ix+1]       
        obj = outputs[ix+2]
        grid[y][x] = "@" if obj == 1 else "#" if obj == 2 else "T" if obj == 3 else "o" if obj == 4 else " "

        ix += 3

def print_grid(grid):
    for row in grid:
        for item in row:
            print(str(item), end='')
        print()
    print()

machine = Machine("Arcade", fields, [])

i = 1
blocks = 0
outputs = []
while not machine.halted:
    out = machine.run()
    outputs.append(out)
    if i%3 == 0:
        if out == 2:
            blocks += 1
    i += 1

print(str(blocks))

# part 2
grid = [["." for i in range(0, 40)] for i in range(0, 26)]

update_grid(grid, outputs)
print_grid(grid)

fields_copy[0] = 2

machine = Machine("Play", fields_copy, [])

pad_x = 0
while not machine.halted:
    x = machine.run()
    y = machine.run()
    tile = machine.run()

    if x == -1 and y == 0:
        print("score: " + str(tile))
        continue

    machine.clear_inputs()
    inp = 0
    if tile == 4: # ball updated > move paddle accordingly
        if x > pad_x:
            inp = 1 # right
        elif x < pad_x:
            inp = -1 # left
    if tile == 3: # paddle
        pad_x = x

    machine.add_input(inp)