def size(t1, t2):
    return (abs(t1[0] - t2[0])+1) * (abs(t1[1] - t2[1])+1)

def part1(tiles):
    max_size = 0
    results = {}
    for t, t1 in enumerate(tiles):
        for t2 in tiles[t+1:]:
            s = size(t1, t2) 
            results [(tuple(t1), tuple(t2))] = s
            if s > max_size:
                max_size = s
    return max_size, results

def is_inside(tile1, tile2, tiles):
    xmin, xmax = sorted([ tile1[0], tile2[0] ])
    ymin, ymax = sorted([ tile1[1], tile2[1] ])

    # check if any edge of the rectangle intersects with the edges of the big polygon (tiles)
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % len(tiles)]
        if y1 == y2: # horizontal edge
            if ymin < y1 < ymax and (min(x1, x2) <= xmin < max(x1, x2) or min(x1, x2) < xmax <= max(x1, x2)):
                return False
        elif x1 == x2: # vertical edge
            if xmin < x1 < xmax and (min(y1, y2) <= ymin < max(y1, y2) or min(y1, y2) < ymax <= max(y1, y2)):
                return False
    return True

def part2(tiles, sizes):
    # Sort sizes by value descending
    sorted_sizes = sorted(sizes.items(), key=lambda x: x[1], reverse=True)

    # Iterate through sorted sizes and return the first one that lies completely within the big polygon
    for (t1, t2), s in sorted_sizes:
        if is_inside(t1, t2, tiles):
            return s
        
    return 0

def main():
    input = open("inputs/9.sam").readlines()

    data = [line.strip() for line in input if line.strip() != '']
    tiles = [[int(x) for x in coord.split(',')] for coord in data]

    max, sizes = part1(tiles)
    print("I: \t", max)
    print("II: \t", part2(tiles, sizes))

if __name__ == "__main__":
    main()