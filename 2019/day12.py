from math import gcd
from functools import reduce

class Moon:
    def __init__(self,name,x,y,z):
        super().__init__()
        self.name = name
        
        self.pos = [x,y,z]
        self.vel = [0,0,0]

        self.start_pos = self.pos[:]
        self.start_vel = self.vel[:]

        self.cycle_time = [-1,-1,-1]
        self.steps = 0

        self.first_cycle = 0
    
    def update_vel(self, other):
        attr = [int(0) if other.pos[i] == self.pos[i] else int((other.pos[i] - self.pos[i]) / abs(other.pos[i] - self.pos[i])) for i in range(0, len(self.pos))]
        self.vel = [(self.vel[i] + attr[i]) for i in range(0, len(self.vel))]

    def update_pos(self, step):
        self.pos = [(self.pos[i] + self.vel[i]) for i in range(0, len(self.pos))]
        self.cycled(step)

    def energy(self):
        pot = sum(abs(p) for p in self.pos)
        kin = sum(abs(v) for v in self.vel)

        return pot * kin

    def print(self):
        print("%s @ %s , vel %s" %(self.name, str(self.pos), str(self.vel)))
    
    def cycled(self, step):
        if self.cycle_time[0] >= 0 and self.cycle_time[1] >= 0 and self.cycle_time[2] >= 0:
            return

        for i in range(0,3):
            if self.cycle_time[i] < 0 and self.pos[i] == self.start_pos[i] and self.vel[i] == self.start_vel[i]:
                self.cycle_time[i] = step

def lcm(a, b):
  return (a * b) // gcd(a, b)

moons = [Moon("a", -3, 15, -11), Moon("b", 3, 13, -19), Moon("c", -13, 18, -2), Moon("d", 6, 0, -1)]
'''
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
'''
#moons = [Moon("a",-1,0,2), Moon("b",2,-10,-7), Moon("c",4,-8,8), Moon("d",3,5,-1)]

'''
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
'''
#moons = [Moon("a",-8,-10,0), Moon("b",5,5,10), Moon("c",2,-7,3), Moon("d",9,-8,-3)]

start_vectors = [[-3,3,-13,6,0,0,0,0],[15,13,18,0,0,0,0,0],[-11,-19,-2,-1,0,0,0,0]]
cycle = [0,0,0]
for t in range(1, 10000):
    for moon1 in moons:
        for moon2 in moons:
            if moon1.name == moon2.name:
                continue
            moon1.update_vel(moon2)

    for moon in moons:
        moon.update_pos(t)

    # check for cycle
    for i in range(0, 3):
        v = [m.pos[i] for m in moons]
        v.extend([m.vel[i] for m in moons])
        print(v)
        if v == start_vectors[i]:
            cycle[i] = t


energy = 0
for moon in moons:
    energy += moon.energy()

print("Total energy: " + str(energy))
print("Cycle: " + str(cycle))
    
print(str([m.cycle_time[0] for m in moons]))
print(str([m.cycle_time[1] for m in moons]))
print(str([m.cycle_time[2] for m in moons]))
#x_cycle = int(least_mult([m.cycle_time[0] for m in moons]))
#y_cycle = int(least_mult([m.cycle_time[1] for m in moons]))
#z_cycle = int(least_mult([m.cycle_time[2] for m in moons]))
x_cycle = reduce(lcm, [m.cycle_time[0] for m in moons])
y_cycle = reduce(lcm, [m.cycle_time[1] for m in moons])
z_cycle = reduce(lcm, [m.cycle_time[2] for m in moons])

print("LCM X: " + str(x_cycle))
print("LCM Y: " + str(y_cycle))
print("LCM Z: " + str(z_cycle))

big_cycle = reduce(lcm, [x_cycle, y_cycle, z_cycle])

print("result: " + str(big_cycle))
print(str(x_cycle))

#[286332, 231614, 60424]
#500903629351944