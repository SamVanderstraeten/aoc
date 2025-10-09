file = open("input/5.sam", "r")
lines = file.readlines()

def codeToNumber(s, c1='B', c0='F'):
    s = s.replace(c1,'1').replace(c0,'0')
    return int(s, 2)

results = []
for line in lines:
    line = line.strip()
    row = line[:-3]
    col = line[-3:]

    rown = codeToNumber(row)
    coln = codeToNumber(col, 'R', 'L')

    results.append(rown*8+coln)

# Part I
print(max(results))

# Part II
results = [int(a) for a in results]
results.sort()

for i, r in enumerate(results):
    if (results[r+1]-results[r] > 1):
        print(str(results[r] + 1))
        break