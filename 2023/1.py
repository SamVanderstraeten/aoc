file = open("input/1.sam", "r")

n = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def first(s):
    minnum = ''
    k = 999
    for num in n:
        i = s.find(num)
        if i == -1: continue
        if i < k:
            k = i
            minnum = num
    return minnum if minnum.isdigit() else str(n.index(minnum)+1)

def last(s):
    maxnum = ''
    k = -1
    for num in n:
        i = s.find(num)
        if i == -1: continue
        if i > k:
            k = i
            maxnum = num
    return maxnum if maxnum.isdigit() else str(n.index(maxnum)+1)
        

d = [(first(s) + last(s)) for s in file.readlines()]
print("Part II:", sum([int(x) for x in d]))