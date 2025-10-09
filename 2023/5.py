file = open("input/5.sam", "r")
lines = file.read()

class Range:
    def __init__(self, src_start, dest_start, range):
        self.src_start = src_start
        self.src_end = src_start + (range-1)
        self.dest_start = dest_start
        self.dest_end = dest_start + (range-1)

    def contains(self, n):
        return n >= self.src_start and n <= self.src_end

    def convert(self, n):
        if not self.contains(n):
            return -1
        return self.dest_start + (n - self.src_start)
    
    def __str__(self):
        return f"{self.src_start}-{self.src_end} -> {self.dest_start}-{self.dest_end}"

class Mapper:
    def __init__(self, data):
        self.ranges = []
        for (i, line) in enumerate(data):
            if i == 0:
                self.name = line.split(" ")[0]
            else:
                [src, dest, range] = line.split(" ")
                self.ranges.append(Range(int(dest), int(src), int(range)))

    def convert(self, n):
        for range in self.ranges:
            if range.contains(n):
                return range.convert(n)
        return n

seeds = []
blocks = lines.split("\n\n")
mappers = []
for (i, block) in enumerate(blocks):
    if i==0: # get seeds
        seeds = [int(n) for n in block.split(": ")[1].split(" ")]
    else: # parse block
        mappers.append(Mapper(block.split("\n")))

results = []
for seed in seeds:
    for mapper in mappers:
        seed = mapper.convert(seed)
    results.append(seed)
print(min(results))

min = 999999999
for (i, seed) in enumerate(seeds):
    if i % 2 == 0:
        print(f'Checking seed {i} ({seed})')
        for k in range(seed, seed+seeds[i+1]):
            if k%100000 == 0:
                print(f'Checking {k}')
            r = k
            for mapper in mappers:
                r = mapper.convert(r)
            if r < min:
                min = r
print(min)