import statistics, math
file = open("input/7.sam", "r")
crabs = [int(x) for x in file.readline().split(",")]

median = round(statistics.median(crabs))
fuel = sum([abs(median-x) for x in crabs])
print("Part I: ",fuel)

def cost(i):
    return i * (i/2) + (i/2) if i%2==0 else i * math.ceil(i/2)

avg_f = math.floor(statistics.mean(crabs))
avg_c = math.ceil(statistics.mean(crabs))
fuel_f = int(sum([cost(abs(avg_f-x)) for x in crabs]))
fuel_c = int(sum([cost(abs(avg_c-x)) for x in crabs]))
print("Part II: ", min(fuel_c, fuel_f))