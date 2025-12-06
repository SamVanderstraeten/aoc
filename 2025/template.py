def part1(data):
    return 0

def part2(data):
    return 0


def main():
    input = open("inputs/6.sam").readlines().strip()

    data = [line.strip() for line in input if line.strip() != '']

    print("I: \t", part1(data))
    print("II: \t", part2(data))

if __name__ == "__main__":
    main()