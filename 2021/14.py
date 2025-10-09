from collections import defaultdict
file = open("input/14.sam", "r")
lines = file.readlines()
polymer = lines[0].strip()
map = dict(x.strip().split(" -> ") for x in lines[2:])

counter = defaultdict(int)
pairs = defaultdict(int)
def develop():
    for pair, amount in pairs.copy().items():
        pairs[pair] -= amount
        d = map[pair]
        pairs[pair[0]+d] += amount
        pairs[d+pair[1]] += amount
        counter[d] += amount

for i in range(len(polymer)):
    counter[polymer[i]] += 1
    if i < len(polymer)-1:
        pairs[polymer[i:i+2]] += 1

for i in range(10):
    develop()
print("Part I", max(counter.values())-min(counter.values()))
for i in range(30): # did 10 loops already
    develop()
print("Part II", max(counter.values())-min(counter.values()))