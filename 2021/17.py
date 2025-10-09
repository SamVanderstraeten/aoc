file = open("input/17.sam", "r")
line = file.readline()
y_min,y_max = map(int,line.strip().split("y=")[1].split(".."))
x_min,x_max = map(int,line.strip().split(",")[0].split("x=")[1].split(".."))

highest = -1
results = []
for start_vel in range(y_min*2,abs(y_min)):
    y_vel = start_vel
    y=0
    current_max_y_val = -1
    while y>=y_min:
        y += y_vel
        y_vel -= 1
        current_max_y_val = max(current_max_y_val,y)
        if y_min<=y<=y_max: # within range
            highest = max(highest, current_max_y_val)
            results.append((abs(start_vel-y_vel), start_vel)) # number of iterations + start velocity Y
print("Part I:",highest)

c = set()
for r in results:
    for start_vel in range(0, x_max+1):
        x=sum([n for n in range(0,start_vel+1)][-r[0]:])
        if x_min<=x<=x_max:
            c.add((start_vel,r[1]))
print("Part II:",len(c))