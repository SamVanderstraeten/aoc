import math
file = open("input/18.sam", "r")
numbers = file.readlines()
snail_nums = []
for num in numbers:
    depth_map = []
    depth = 0
    for c in num:
        if c=="[":
            depth+=1
        elif c=="]":
            depth-=1
        elif c.isnumeric():
            depth_map.append((int(c),depth))
    snail_nums.append(depth_map)

def explode_pairs(sum):
    for i,n in enumerate(sum):
        if n[1] == 5 and (i+1)<len(sum) and sum[i+1][1] == 5: # exploding pair
            if i > 0:
                sum[i-1] = (sum[i-1][0] + n[0], sum[i-1][1])
            if i+2 < len(sum):
                sum[i+2] = (sum[i+2][0] + sum[i+1][0], sum[i+2][1])
            sum[i] = (0,sum[i][1]-1)
            del sum[i+1]
            return True
    return split_nums(sum)

def split_nums(sum):
    for i,n in enumerate(sum):
        if n[0] > 9:
                sum[i] = (int(math.floor(n[0]/2)), n[1]+1)
                sum.insert(i+1, (int(math.ceil(n[0]/2)), n[1]+1))
                return True
    return False

def magnitude(n):
    num = n.copy()
    while len(num) > 1:
        for i in range(len(num)-1):
            if num[i][1]==num[i+1][1]:
                num[i] = (3*num[i][0]+2*num[i+1][0], num[i][1]-1)
                del num[i+1]
                break # is this a good idea?
    return num[0][0]    

def calc(num):
    while True:
        if not explode_pairs(num):
            break
    return num

sum = snail_nums[0]
for i, sn in enumerate(snail_nums):
    if i==0:continue
    sum = [(s[0],s[1]+1) for s in sum+sn]  
    sum = calc(sum)
print("Part I",magnitude(sum))

m = 0
for x in snail_nums:
    for y in snail_nums:
        if x!=y:
            s1 = magnitude(calc([(s[0],s[1]+1) for s in x+y]))
            s2 = magnitude(calc([(s[0],s[1]+1) for s in y+x]))
            m = max(m,s1,s2)
print("Part II",m)