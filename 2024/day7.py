def part1(ns, solutions):
    for i in range(len(ns)):
        numbers = ns[i]
        solution = solutions[i]

        

    return 0

def part2(eqs):
    return 0

def main():
    input = open("inputs/day7.txt").read().strip()
    eqs = [l.split(": ") for l in input.splitlines()]

    numbers = []
    solutions = []
    for eq in eqs:
        list = [int(x) for x in eq[1].strip().split(" ")]
        solution = int(eq[0])

        numbers.append(list)
        solutions.append(solution)

    print(part1(numbers, solutions))
    print(part2(eqs))


if __name__ == "__main__":
    main()