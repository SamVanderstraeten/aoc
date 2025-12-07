from util.parser import Parser

def part2(grid):
    solutions = {}
    for r in range(len(grid)-1, -1, -1):
        row = grid[r]
        for c in range(len(row)):
            char = row[c]
            if char == "^" or char == "S":
                duo_sum = 0
                left = c-1 if c-1 >= 0 else None
                right = c+1 if c+1 < len(row) else None

                for d in [left, right]:
                    for n in range(r+1, len(grid)):
                        tup = (n, d)
                        if tup in solutions.keys():
                            duo_sum += solutions[tup]
                            break
                        if n == len(grid)-1:
                            duo_sum += 1

                if (r, c) not in solutions.keys():
                    solutions[(r, c)] = duo_sum
    
    return solutions[(0, grid[0].index("S"))]
                    
def part1(grid):
    streams = []
    streams.append(grid[0].index("S"))
    splits = 0
    
    for r in range(1, len(grid)):
        row = grid[r]
        newstreams = []
        for s in streams:
            if row[s] == "^":
                splits += 1
                if s-1 >= 0:
                    newstreams.append(s-1)
                if s+1 < len(row):
                    newstreams.append(s+1)
            else:
                newstreams.append(s)
        streams = set(newstreams)

    return splits

def main():
    input = open("inputs/7.sam")
    lines = [l.strip() for l in input.readlines()]
    grid = Parser.parse_grid(lines, delim="")

    print("Part I: \t", part1(grid))
    print("Part II: \t", part2(grid))

if __name__ == "__main__":
    main()