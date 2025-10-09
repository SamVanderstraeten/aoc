def part1(left, right):
    return sum(abs(x - y) for x, y in zip(left, right))

def part2(left, right):
    return sum(right.count(x) * x for x in left)

def main():
    input = open("inputs/day1.txt").read().strip()
    duos = [z.split("   ") for z in input.splitlines()]
    left = [int(x) for x, y in duos]
    right = [int(y) for x, y in duos]

    left.sort()
    right.sort()

    print(part1(left, right))
    print(part2(left, right))


if __name__ == "__main__":
    main()