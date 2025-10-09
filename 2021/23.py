from util.parser import Parser
from util.printer import Printer
file = open("input/23b.sam", "r")
lines = file.readlines()
grid = Parser.parse_grid(lines,'',{},False)
pod_cost={'A':1,'B':10,'C':100,'D':1000}
room_entries={'A':2,'B':4,'C':6,'D':8}
pod_targets={'A':[11,12,13,14],'B':[15,16,17,18],'C':[19,20,21,22],'D':[23,24,25,26]}
pod_rooms={11:'A',12:'A',13:'A',14:'A',15:'B',16:'B',17:'B',18:'B',19:'C',20:'C',21:'C',22:'C',23:'D',24:'D',25:'D',26:'D'}
room_exits={11:2,12:2,13:2,14:2,15:4,16:4,17:4,18:4,19:6,20:6,21:6,22:6,23:8,24:8,25:8,26:8}

def grid_to_str(grid):
    return "".join(grid[1][1:-1])+grid[2][3]+grid[3][3]+grid[4][3]+grid[5][3]+grid[2][5]+grid[3][5]+grid[4][5]+grid[5][5]+grid[2][7]+grid[3][7]+grid[4][7]+grid[5][7]+grid[2][9]+grid[3][9]+grid[4][9]+grid[5][9]

def in_some_room(i):
    return i>10

def in_target_room(i,c):
    return i in pod_targets[c]

def first_spot(i):
    return i in [11,15,19,23]

def second_spot(i):
    return i%2==0

def blocked(i,above):
    return not first_spot(i) and above != '.'

def room_available(c, state):
    for t in pod_targets[c].__reversed__():
        if state[t] != '.' and state[t] != c:
            return False
    return True

def free_spot_in_room(c, state):
    for t in pod_targets[c].__reversed__():
        if state[t] == '.':
            return t
    return -1

def pod_in_place(state,i,c):
    for t in pod_targets[c].__reversed__():
        if t >= i and state[t] != c:
            return False
    return True

def get_accessible_room_points(state, i, c):
    room_entry=room_entries[c]
    dir = int((room_entry-i)/abs(i-room_entry))
    dist=0
    for d in range(1,abs(i-room_entry)+1):
        dist += 1
        if state[i+(dir*d)] != '.':
            return []
    
    r=[]
    spot = free_spot_in_room(c, state)
    return [(spot, dist+1+pod_targets[c].index(spot))]

def get_accessible_hallway_points(state, i, c):
    room_exit=room_exits[i]
    k=pod_rooms[i]
    dist=abs(i-min(pod_targets[k]))+1
    hallway=[]
    for d in range(1,room_exit+1):
        if state[room_exit-d] == '.':
            dist+=1
            if not (room_exit-d) in room_exits.values():
                hallway.append((room_exit-d, dist))            
        else:
            break
    dist=abs(i-min(pod_targets[k]))+1
    for d in range(1,11-room_exit):
        if state[room_exit+d] == '.':
            dist+=1
            if not (room_exit+d) in room_exits.values():
                hallway.append((room_exit+d,dist))            
        else:
            break
    return hallway

moves={grid_to_str(grid): 0}
def resolve_next():
    global moves
    moves = dict(sorted(moves.items(), key=lambda item: item[1]))
    state = list(moves.keys())[0]
    energy = moves.pop(state)
    if state[11:] == "AAAABBBBCCCCDDDD":
        return energy

    banks = 0
    moveout = {}
    for i,c in enumerate(state):
        if c==".":continue
        if in_target_room(i,c) and pod_in_place(state,i,c):continue # not continued for pod in place
        
        if not in_some_room(i) and room_available(c,state):
            points = get_accessible_room_points(state,i,c)
            if len(points) > 0:
                for p,d in points:
                    # move to point, add state to 'moves'
                    s=[x for x in state]
                    s[p] = c
                    s[i] = '.'
                    s=''.join(s)
                    if not s in moves.keys() or moves[s] > energy+d*pod_cost[c]:
                        moves[s] = energy+d*pod_cost[c]
                        banks+=1
        
        # only do this if no banks are possible
        if banks==0 and in_some_room(i) and not blocked(i,state[i-1]):
            # exit room and visit all accessible points
            points = get_accessible_hallway_points(state, i, c)
            if len(points) > 0:
                for p,d in points:
                    # move to point, add state to 'moves'
                    s=[x for x in state]
                    s[p] = c
                    s[i] = '.'
                    s=''.join(s)
                    if not s in moveout.keys() or moveout[s] > energy+d*pod_cost[c]:
                        moveout[s] = energy+d*pod_cost[c]
    
    if banks == 0:
        for m in moveout.keys():
            if not m in moves.keys() or moves[m] > moveout[m]:
                moves[m] = moveout[m]
    return -1

while True:
    energy = resolve_next()
    if energy > 0:
        print(energy)        
        break