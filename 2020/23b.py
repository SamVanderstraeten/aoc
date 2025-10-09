cfg = "315679824"
#cfg = "389125467"
cfg = [int(c) for c in cfg]

LOOPS = 10000000
MAX = 1000000

config = {}
for i, n in enumerate(cfg):
    if i+1 < len(cfg):
        config[n] = cfg[i+1]

prev = cfg[-1]
for i in range(10,MAX+1):
    config[prev] = i
    prev = i
config[MAX] = cfg[0]

current = 3
for i in range(0,LOOPS):
    if (i%(MAX/100)) == 0:
        print("...",i/(MAX/100)),"%")
    sub = [config[current], config[config[current]], config[config[config[current]]]]
    after  = current - 1
    if after == 0:
        after = MAX
    while after in sub:
        after -= 1
        if after == 0:
            after = MAX
    ll = config[after]
    config[current] = config[sub[2]]
    config[after] = sub[0]
    config[sub[2]] = ll
    current = config[current]
s = config[1]
print(s*config[s])