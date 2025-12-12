def part1(regions):
    count = 0
    for (x,y,region) in regions:
        count += sum(region) * 7 < x * y
    return count # number of regions where it would be theoretically possible to fit all shapes

def part2(data):
    return 0

def main():
    input = open("inputs/12.sam").read()

    comps = input.split("\n\n")
    regions = []

    r = comps[-1].split("\n")
    for region_line in r:
        rl = region_line.split(": ")
        (x,y) = map(int, rl[0].split("x"))
        region = list(map(int, rl[1].split(" ")))
        regions.append((x,y,region))

    print("I: \t", part1(regions))
    print("II: \t", part2(regions))

if __name__ == "__main__":
    main()