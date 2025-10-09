from stepmachine import Machine

file = open("input/day23.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]

num = 50
pcs = [Machine("Computer %d"%(x), fields, [x]) for x in range(num)]

packets = {}

i=0
found = False
all_idle = True
nat = None
prev_nat_y = None
first = True
while not found:
    i+=1
    all_idle = True
    for pc in pcs:
        o1 = pc.run()
        o2 = pc.run()

        if isinstance(o1, list) or isinstance(o2, list):
            continue

        all_idle = False
        o3 = pc.run()
        
        if o1 == 255:
            if first:
                print("First Y-value to NAT: " + str(o3))
            nat = (o2, o3)
            first = False
        else:
            pcs[o1].add_input(o2)
            pcs[o1].add_input(o3)        
    
    if all_idle and not nat == None:
        if prev_nat_y == nat[1]:
            print("Repeated Y-value: " + str(prev_nat_y))
            break
        else:
            pcs[0].add_input(nat[0])
            pcs[0].add_input(nat[1])
            prev_nat_y = nat[1]
        