file = open("input/day6.txt", "r")
lines = file.readlines()

orbitalMap = {}
planet_list = []

for line in lines:
    planets = line.strip("\n").split(")")
    orbitalMap[planets[1]] = planets[0] # planets[0] is in orbit around planets[1]

# Find path to COM for X
def get_path(x):
    path = []
    while not x == "COM":
        x = orbitalMap[x]
        path.append(x)
    return path

# Count back for every planet in orbital map
total = 0
for planet in orbitalMap.keys():
    path = get_path(planet)
    total += len(path)

print("Checksum: " + str(total))

you = get_path("YOU")
san = get_path("SAN")

# Find first common point in path
for i in range(0,len(you)):
    planet = you[i]
    if planet in san:
        transfer = i + san.index(planet)
        print("Path length: " + str(transfer))
        break
