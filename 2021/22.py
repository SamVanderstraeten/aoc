file = open("input/22.sam", "r")
lines = file.readlines()
instr = []
bounds = None #[[-50,50],[-50,50],[-50,50]]

def intersect(v,w): # 
    if (v[0][0] <= w[0][0] <= v[0][1] or v[0][0] <= w[0][1] <= v[0][1] or w[0][0] <= v[0][0] <= w[0][1] or w[0][0] <= v[0][1] <= w[0][1]) and (v[1][0] <= w[1][0] <= v[1][1] or v[1][0] <= w[1][1] <= v[1][1] or w[1][0] <= v[1][0] <= w[1][1] or w[1][0] <= v[1][1] <= w[1][1]) and (v[2][0] <= w[2][0] <= v[2][1] or v[2][0] <= w[2][1] <= v[2][1] or w[2][0] <= v[2][0] <= w[2][1] or w[2][0] <= v[2][1] <= w[2][1] ):
        xmid = sorted([v[0][0], v[0][1], w[0][0], w[0][1]])[1:-1]
        ymid = sorted([v[1][0], v[1][1], w[1][0], w[1][1]])[1:-1]
        zmid = sorted([v[2][0], v[2][1], w[2][0], w[2][1]])[1:-1]
        return [[xmid[0],xmid[1]], [ymid[0],ymid[1]],[zmid[0],zmid[1]]]
    return None

def volume(v):
    if v == None: return 0
    return ((abs(v[0][0]-v[0][1])+1) * (abs(v[1][0]-v[1][1])+1) * (abs(v[2][0]-v[2][1])+1))

for line in lines:
    onoff,coords = line.split(" ")
    coords = [[int(n) for n in x.split("=")[1].split("..")] for x in line.strip().split(",")]
    if bounds != None:
        coords = intersect(coords, bounds)
    instr.append([onoff, coords])

total = 0
on_cubes = []
off_cubes = []
for ix,i in enumerate(instr):
    if i[1] == None:continue
    ons = on_cubes.copy()
    offs = off_cubes.copy()
    for on in ons:
        s = intersect(i[1], on)
        if s != None:
            off_cubes.append(s) 
            total -= volume(s)           
    for off in offs:
        s = intersect(i[1], off)
        if s != None:
            on_cubes.append(s)
            total += volume(s)
    if i[0] == "on":
        on_cubes.append(i[1])
        total += volume(i[1])

print("Part I/II:",(total)) # switch 'bounds' on top for part I