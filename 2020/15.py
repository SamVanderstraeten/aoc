list = [0,20,7,16,1,18,15]

mem = {}
last = -1
for n in range(0,len(list)-1):
    mem[list[n]] = n

last = list[len(list)-1]

# speak up
for i in range(len(list)-1, 30000000-1):
    if not last in mem.keys():
        speak = 0
    else:
        speak = i - mem[last]
    mem[last] = i
    last = speak
print(last)