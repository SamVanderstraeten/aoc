lower = 272091
upper = 815432
count = 0

def check_number(nr):
    adjs = {}
    prev_c = '0'
    
    for c in str(nr):
        if int(c) < int(prev_c):# decrease > return false
            return False
        if c == prev_c:         # adjacent, count number of o
            adjs[c] += 1
        else:
            adjs[c] = 1

        prev_c = c
    
    #return any(x in adjs.values() for x in [2,3,4,5,6])
    return 2 in adjs.values()

for i in range(lower, upper):
    if check_number(i):
        count += 1

print(str(count))