#config = "389125467"
config = "315679824"
config = [c for c in config]

for i in range(10,1000001):
    config.append(str(i))

LOOPS = 10000000

current = 0
for i in range(0,LOOPS):
    if (i%1000) == 0:
        print("LOOP", i)
    current_num = int(config[current])
    #print(current,"->",current_num)
    start = (current + 1) % len(config)
    end = (start + 3) % len(config)
    sub = []
    for x in range(0,3):
        if current == len(config):
            current -= 1
        cx = (current + 1) % len(config)
        sub.append(str(config[cx]))
        del config[cx]
    #print("Sub", sub)
    #print("Config", config)
    next_num = current_num - 1
    while not str(next_num) in config:
        next_num -= 1
        if next_num < 0:
            next_num = int(max(config))
    #print("Place sub after",next_num,"(",config.index(str(next_num)),")")

    sub.reverse()
    for s in sub:
        config.insert(config.index(str(next_num))+1, s)

    '''adjust current to be true next (based on prev)
    OR
    rearrange all'''

    #print(config)
    current = (config.index(str(current_num))+1) % len(config) 
    #print("next current",current)

s = config.index("1")
#r = config[s+1:] + config [:s]
#print(''.join(r))
print(config[s+1]+" "+config[s+2])