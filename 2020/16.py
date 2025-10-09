import math

file = open("input/16.sam", "r")
lines = file.readlines()

bounds = []
fields = []

for line in lines:
    split = line.strip().split(" ")
    if len(split) < 2:
        break
    bound = []
    bound.append(int(split[-1].split("-")[0]))
    bound.append(int(split[-1].split("-")[1]))
    bound.append(int(split[-3].split("-")[0]))
    bound.append(int(split[-3].split("-")[1]))
    bounds.append(bound)
    fields.append(line.split(":")[0])

print(fields)
print(bounds)

error = 0
nbt = False
classmap = {}
for line in lines:
    if line.strip() == "nearby tickets:":
        nbt = True
        continue
    if not nbt:
        continue

    valid_line = True
    nums = line.strip().split(",")
    nums = [int(n) for n in nums]
    linemap = {}
    for i in range(0, len(nums)):
        n = nums[i]
        valid = False
        linemap[i] = []
        for b in range(0,len(bounds)):
            bound = bounds[b]
            if bound[0] <= n <= bound[1] or bound[2] <= n <= bound[3]:
                linemap[i].append(fields[b])
                valid = True
        if not valid:
            error += n
            valid_line = False
    if valid_line:
        # transfer possibilities
        for key in linemap.keys():
            newclassmap = []
            for c in linemap[key]:
                if (not key in classmap) or (c in classmap[key]):
                    newclassmap.append(c)
            classmap[key] = newclassmap

# cleanup
improved = True
while improved:
    improved = False
    for c in classmap:
        if len(classmap[c]) == 1:
            for k in classmap:
                if classmap[c][0] in classmap[k] and k != c:
                    classmap[k].remove(classmap[c][0])
                    improved = True
            if improved:
                break

fieldmap = {}
for c in classmap:
    fieldmap[classmap[c][0]] = int(c)

my_ticket = [157,73,79,191,113,59,109,61,103,101,67,193,97,179,107,89,53,71,181,83]

# mult
mult = math.prod([my_ticket[fieldmap[f]] for f in fieldmap if "departure" in f])

print(error)
print(mult)
