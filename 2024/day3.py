import re

def part1(s):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = [(int(x), int(y)) for x,y in re.findall(pattern, s)]      
    return sum([x*y for x,y in matches])

def part2(s):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, s)
    total = 0

    for match in matches:
        x, y = map(int, match.groups())
        loc = match.start()

        rev = s[:loc][::-1]
        do_pattern = r"\)\(od"
        dont_pattern = r"\)\(t'nod"

        do_match = re.search(do_pattern, rev)
        dont_match = re.search(dont_pattern, rev)

        if do_match and (not dont_match or do_match.start() < dont_match.start()):
            total += x * y
        elif not do_match and not dont_match:
            total += x * y
    return total

def main():
    input = open("inputs/day3.txt").read().strip()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()