import numpy as np
file = open("input/19.sam", "r")
lines = file.readlines()
scanners = []
beacons = []
for line in lines:
    if line=="\n":
        scanners.append(beacons)
    elif line.strip()[-1]=='-':
        beacons = []
    else:
        beacons.append(tuple([int(x) for x in line.strip().split(",")]))
scanners.append(beacons)

def dist(a,b):
    return ( ( ((a[0]-b[0])**2) + ((a[1]-b[1])**2) + ((a[2]-b[2])**2) ) ** (1/2))

def manhattan_dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

def beacons_dists(beacons):
    dists = np.zeros((len(beacons),len(beacons)))
    for i,a in enumerate(beacons):
        for j,b in enumerate(beacons):
            if i != j:
                dists[i,j] = dists[j,i] = dist(a,b)
    return dists

def resolve_scanner_location(beacons_a, beacons_b):
    s = []
    for x in range(len(beacons_a)):
        k = []
        for a in beacons_a[x]:
            r = []
            for b in beacons_b[x]:
                for i in [-1,1]:
                    r.append(a-i*b)
            k.append(r)
        if len(s) == 0:
            s = k
        else:
            for i in range(3):
                if not isinstance(s[i], int):
                    s[i] = list(set(s[i]).intersection(k[i]))
                    if len(s[i]) == 1:
                        s[i] = s[i][0]
                    elif len(s[i]) == 0:
                        s[i] = s[i]+k[i]
    return (s[0],s[1],s[2])

# Map beacons_b to beacons_a space, using vector
def map_beacons(beacons_b, vector, overlapping_pair):
    mapped_beacons = [[0,0,0] for i in range(len(beacons_b))]
    for ia,a in enumerate(overlapping_pair[0]):
        for ib,b in enumerate(overlapping_pair[1]):
            for i in [-1,1]:
                if a-i*b == vector[ia]:
                    for index,beacon in enumerate(beacons_b):
                        mapped_beacons[index][ia] = vector[ia]+i*beacon[ib]
    return [tuple(b) for b in mapped_beacons]

def tuple_sum(a,b):
    return tuple(map(lambda x, y: x + y, a, b))

for i, scanner in enumerate(scanners):
    bdists = beacons_dists(scanner)
    scanners[i] = {'beacons': scanner, 'beacon_dists': bdists}

scanner_locations = []
def iterate_scanners(scanboi):
    scanners = scanboi.copy()
    for ii, one_scanner in enumerate(scanners):
        for i, other_scanner in enumerate(scanners):
            if i == ii: continue
            scanner1_common = []
            scanner2_common = []
            for bi, beacon1 in enumerate(one_scanner['beacon_dists']):
                for bj, beacon2 in enumerate(other_scanner['beacon_dists']):
                    its = list(set(beacon1).intersection(beacon2))
                    if len(its) >= 12:
                        scanner1_common.append(one_scanner['beacons'][bi])
                        scanner2_common.append(other_scanner['beacons'][bj])
            if len(scanner1_common) > 0:
                vector = resolve_scanner_location(scanner1_common, scanner2_common)
                scanner_locations.append(vector)
                mapped_beacon_locations = map_beacons(other_scanner['beacons'], vector, [scanner1_common[0],scanner2_common[0]])
                one_scanner['beacons'] += mapped_beacon_locations
                one_scanner['beacons'] = list(set(one_scanner['beacons']))
                one_scanner['beacon_dists'] = beacons_dists(one_scanner['beacons'])
                del scanners[i]
                return scanners
    return scanners

while len(scanners) > 1:
    scanners = iterate_scanners(scanners)
print("Part I:",len(scanners[0]['beacons'])) #omgthatwasuglykthxbye

d = 0
for i,a in enumerate(scanner_locations):
    for j,b in enumerate(scanner_locations):
        if i != j:
            d = max(d, manhattan_dist(a,b))
print("Part II",d) 