import math

NUM_ITERATIONS = 1000

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)        

class Circuit:
    def __init__(self,start_box):
        self.boxes = [start_box]
    
    def add_box(self, box):
        self.boxes.append(box)

    def empty(self):
        self.boxes = []
    
    def size(self):
        return len(self.boxes)    

# all circuits are disjoint at the beginning, containing one box each
# empty circuits remain in the circuits list, so indices are not screwed up
def join_circuits(box_a, box_b, box_store):
    circuit_a = box_store[(box_a.x, box_a.y, box_a.z)]
    circuit_b = box_store[(box_b.x, box_b.y, box_b.z)]

    if circuit_a != circuit_b:
        # Join circuits
        for box in circuit_b.boxes:
            circuit_a.add_box(box)
            box_store[(box.x, box.y, box.z)] = circuit_a

        circuit_b.empty()
        return True
    return True

def part1(boxes, circuits, box_store):
    distances = {}
    for c1, circuit in enumerate(circuits):
        for c2, other in enumerate(circuits):
            if c1 != c2:
                distances[(c1,c2)] = circuit.boxes[0].dist(other.boxes[0])

    # Sort distances once, pop them afterwards
    distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    order = list(distances.keys())

    # Get circuits with minimum distance
    _=0
    print("Please stand by, this may take a while...")
    while _ < NUM_ITERATIONS:
        mi, mj = order.pop(0)
        order.pop(0)  # remove the reverse as well

        boxi = boxes[mi]
        boxj = boxes[mj]
        distances[(mi,mj)] = distances[(mj,mi)] = float('inf') # So they are not chosen again
        join_circuits(boxi, boxj, box_store)
        _+=1
    
    sizes = sorted([circuit.size() for circuit in circuits], reverse=True)
    return sizes[0]*sizes[1]*sizes[2]

def part2(boxes, circuits, box_store):
    distances = {}
    for c1, circuit in enumerate(circuits):
        for c2, other in enumerate(circuits):
            if c1 != c2:
                distances[(c1,c2)] = circuit.boxes[0].dist(other.boxes[0])

    # Sort distances once
    distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    order = list(distances.keys())

    # Get circuits with minimum distance
    _=0
    last_size = 0
    num_boxes = len(boxes)
    print("Please stand by, this may take a while...")
    while last_size < num_boxes:
        mi, mj = order.pop(0)
        order.pop(0)  # remove the reverse as well

        boxi = boxes[mi]
        boxj = boxes[mj]
        # check in which circuits they are and join those circuits
        distances[(mi,mj)] = distances[(mj,mi)] = float('inf') # So they are not chosen again
        join_circuits(boxi, boxj, box_store)
        last_size = box_store[(boxi.x, boxi.y, boxi.z)].size()
        _+=1
    
    return boxi.x * boxj.x


def main():
    input = open("inputs/8.sam").readlines()

    boxes = []
    box_store = {}
    circuits = []
    for line in input:
        s = line.strip().split(",")
        box = Box(int(s[0]), int(s[1]), int(s[2]))
        boxes.append(box)
        circuit = Circuit(box)
        box_store[(box.x, box.y, box.z)] = circuit
        circuits.append(circuit)

    #print("I: \t", part1(boxes, circuits, box_store))
    print("II: \t", part2(boxes, circuits, box_store))

if __name__ == "__main__":
    main()