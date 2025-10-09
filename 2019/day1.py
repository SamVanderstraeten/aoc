file = open("input/day1.txt", "r")
lines = file.readlines()

def calc_fuel(weight):
    if weight <= 6:
        return 0
        
    fuel = int(weight / 3) - 2
    return fuel + calc_fuel(fuel)

total = 0
for line in lines:
    total += calc_fuel(int(line))

print(str(total))