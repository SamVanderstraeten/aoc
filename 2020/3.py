file = open("input/3.sam", "r")
lines = file.readlines()

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
mult = 1

for slope in slopes:
    (slope_r, slope_d) = slope
    index = 0
    trees = 0
    skip = False
    print("Slope",slope)
    for line in lines:
        # skip every other line when DOWN slope is 2
        # https://www.youtube.com/watch?v=Trd49Da0gf0
        if slope_d == 2 and skip:
            skip = False
            continue
        skip = True

        line = line.strip()
        if line[index] == "#":
            trees += 1
        index = (index + slope_r) % len(line)
    print(str(trees))
    mult = mult * trees
print(str(mult))