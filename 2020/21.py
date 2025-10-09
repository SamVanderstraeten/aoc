file = open("input/21.sam", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

allergens = {}
ingredients = set()
for line in lines:
    ing, all = line.split(" (contains ")
    for i in ing.split(" "):
        ingredients.add(i)
    for a in all[:-1].split(", "):
        if not a in allergens:
            allergens[a] = ing.split(" ")
        else:
            allergens[a] = [e for e in ing.split(" ") if e in allergens[a]]

values = set()
for k in allergens:
    for v in allergens[k]:
        values.add(v)

for v in values:
    ingredients.remove(v)

count = 0
for line in lines:
    ing, all = line.split(" (contains ")
    for i in ingredients:
        if i in ing.split(" "):
            count += 1
print(count)

for i in range(0,len(allergens.keys())):
    for a in allergens:
        if len(allergens[a]) == 1:
            for d in allergens:
                if a == d:
                    continue
                if allergens[a][0] in allergens[d]:
                    allergens[d].remove(allergens[a][0])
print(allergens)

sortedall=sorted(allergens.keys(), key=lambda x:x.lower())

for s in sortedall:
    print(allergens[s][0]+",",end="")