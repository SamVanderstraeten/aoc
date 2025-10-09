file = open("input/2.sam", "r")
lines = file.readlines()

# Part I
depth = 0
h = 0
for line in lines:
    (instruction, amount) = line.split(" ")
    amount = int(amount)
    if instruction == "up":
        depth -= amount
    elif instruction == "down":
        depth += amount
    elif instruction == "forward":
        h += amount
print(depth*h)

# Part II
depth = 0
h = 0
aim = 0
for line in lines:
    (instruction, amount) = line.split(" ")
    amount = int(amount)
    if instruction == "up":
        aim -= amount
    elif instruction == "down":
        aim +=  amount
    elif instruction == "forward":
        h += amount
        depth += aim*amount
print(depth*h)