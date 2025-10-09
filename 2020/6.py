file = open("input/6.sam", "r")
lines = file.readlines()

qs = set()
total = 0
for line in lines:
    line = line.strip()
    
    for q in line:
        qs.add(q)

    if line == "":
        # end of group
        total += len(qs)
        qs = set()
print(str(total))

# Part II
s = []
first = True
total = 0
for line in lines:
    line = line.strip()

    if first:
        s = line
        first = False

    s = [e for e in line if e in s]
    
    if line == "":
        # end of group
        total += len(s)
        first = True
print(str(total))