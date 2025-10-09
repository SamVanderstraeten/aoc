from stepmachine import Machine

file = open("input/day17.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]
fields_copy = fields[:]

bot = Machine("Bot", fields, [])

grid = [[]]
row = 0
while not bot.halted:
    out = bot.run()

    if bot.halted:
        break

    if out == 35:
        grid[row].append("#")
    elif out == 46:
        grid[row].append(".")
    elif out == 10:
        grid.append([])
        row += 1
    else:
        grid[row].append(str(chr(out)))

# clean up empty rows
while len(grid[-1]) == 0:
    grid = grid[:-1]

for r in range(0, len(grid)):
    for c in range(0, len(grid[r])):
        i = grid[r][c]
        print(str(i), end='')
    print()


sum = 0
for r in range(1, len(grid)-1):
    for c in range(1, len(grid[r])-1):
        #print(str(r) + ","+str(c))
        i = grid[r][c]
        if i == "#" and grid[r+1][c] == "#" and grid[r][c+1] == "#" and grid[r-1][c] == "#" and grid[r][c-1] == "#":
            sum += (r*c)

print(str(sum))

# part 2
# did it manually
'''
    L 12 L 12 R 4 R 10 R 6 R 4 R 4 L 12 L 12 R 4 R 6 L 12 L 12 R 10 R 6 R 4 R 4 L 12 L 12 R 4 R 10 R 6 R 4 R 4 R 6 L 12 L 12 R 6 L 12 L 12 R 10 R 6 R 4 R 4
    Patterns:
    A = L 12 L 12 R 4 
    B = R 6 L 12 L 12 
    C = R 10 R 6 R 4 R 4
    Result:
    A C A B C A C B B C
'''

fields_copy[0] = 2
NEWLINE = 10

main_routine = "A,C,A,B,C,A,C,B,B,C\n"
fun_a = "L,12,L,12,R,4\n"
fun_b = "R,6,L,12,L,12\n"
fun_c = "R,10,R,6,R,4,R,4\n"
debug = "n\n"

inputs = []

def add_all(list, inputs):
    for r in list:
        inputs.append(ord(r))

add_all(main_routine, inputs)
add_all(fun_a, inputs)
add_all(fun_b, inputs)
add_all(fun_c, inputs)
add_all(debug, inputs)

scaf = Machine("Scaffolding", fields_copy, inputs)

while not scaf.halted:
    out = scaf.run()

    try:
        print(str(chr(out)), end='')
    except:
        print(str(out))
