file = open("input/12.sam", "r")
lines = file.readlines()

d = {"N": (0,1), "S": (0,-1), "E": (1,0), "W": (-1,0)}
hs = "NESW"
heading = "E"

def change_heading(curr_heading, curr_wp, dir, degrees):

    ha = [curr_wp[0], curr_wp[1], -curr_wp[0], -curr_wp[1]]

    n = int(degrees / 90)

    rotated_wp = []
    if dir == "R":
        rotated_wp = [ha[n%4], ha[(n+1)%4]]
    elif dir == "L":
        rotated_wp = [ha[(-n)%4], ha[(-n+1)%4]]
    return rotated_wp
    '''
    curr = hs.find(curr_heading)

    if dir == "L":
        curr = (curr - n + len(hs)  ) % len(hs)
    elif dir == "R":
        curr = (curr + n) % len(hs)
    return hs[int(curr)]'''

wp_pos = [10,1]
pos = [0,0]
for line in lines:
    i = line[0]
    num = int(line[1:])
    print(i,num)
    if i == "F":
        pos = [(wp_pos[x]*num+pos[x]) for x in range(0,2)]
    elif i == "L" or i == "R":
        print("old wp", wp_pos)
        wp_pos = change_heading(heading, wp_pos, i, num)
        print("new wp", wp_pos)
    else:
        wp_pos = [(wp_pos[x]+num*d[i][x]) for x in range(0,2)]
    print("WP",wp_pos)
    print("Boat",pos)
print(">>>>",abs(int(pos[0]))+abs(int(pos[1])))

