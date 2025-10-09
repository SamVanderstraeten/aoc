from stepmachine import Machine

file = open("input/day19.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]

# Part I
# Could optimize this a lot... but hey, who cares... :)
scan = 0
for i in range(0,50):
    for j in range(0,50):
        droid = Machine("Droid", fields, [i, j])
        out = droid.run()

        if out == 1:
            scan += 1

print("Part I: " + str(scan))


# Part II
# Only calculate the first of each row (use start pointer to skip unneeded positions)
# When first of row is found: check that position (-100, +100)
# If that is in range as well: bingo! (subtract 100 of first of row and that should be the answer)

SIZE = 100
start_pointer = 0
current_row = SIZE
while(True):
    out = -1
    while not out == 1:
        droid = Machine("Droid", fields, [start_pointer, current_row])
        out = droid.run()        

        if out == 0:
            start_pointer += 1

    # found first of row, check bound
    bound_x = start_pointer + (SIZE-1)
    bound_y = current_row - (SIZE-1)

    droid = Machine("Droid", fields, [bound_x, bound_y])
    out = droid.run()

    if out == 1:
        print("Part II: (%d, %d) => %d"%(start_pointer, bound_y, (start_pointer*10000 + bound_y)))
        break

    current_row += 1


