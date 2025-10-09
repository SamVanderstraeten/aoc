import math

file = open("input/20.sam", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

borders = {}
tile_conn = {}

def add_border(b, tile):
    if not b in borders:
        borders[b] = [tile]
    else:
        borders[b].append(tile)
        for tiler in borders[b]:
            if tiler in tile_conn:
                tile_conn[tiler] += 1
            else:
                tile_conn[tiler] = 1

i = 0
while i < len(lines):
    line = lines[i]
    t, tile_id = line[:-1].split(" ")
    if t == "Tile":
        tile = lines[i+1:i+11]
        i += 11

        add_border(tile[0], tile_id)
        add_border(tile[0][::-1], tile_id)

        add_border(tile[-1], tile_id)
        add_border(tile[-1][::-1], tile_id)

        left = ''.join([k[0] for k in tile])
        add_border(left, tile_id)
        add_border(left[::-1], tile_id)
    
        right = ''.join([k[-1] for k in tile])
        add_border(right, tile_id)
        add_border(right[::-1], tile_id)

    i += 1

pp = [int(k) for k in tile_conn if tile_conn[k] == 4]
m = math.prod(pp)
print(m)