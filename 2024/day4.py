from util.parser import Parser
from util.printer import Printer

def has_valid_corners(grid, r, c):
    h = len(grid)
    w = len(grid[0])

    if r-1 >= 0 and r+1 < h and c-1 >= 0 and c+1 < w:
        d1 = list(grid[r+1][c+1] + grid[r-1][c-1])
        d2 = list(grid[r+1][c-1] + grid[r-1][c+1])

        d1 = "".join(sorted(d1))
        d2 = "".join(sorted(d2))
        if d1 == d2 == "MS":
            return True
    return False

def count_valid_pattern(grid, r, c, pattern):
    dirs = [[0,1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    h = len(grid)
    w = len(grid[0])

    count = 0
    for dr, dc in dirs:
        if 0 <= r+3*dr < h and 0 <= c+3*dc < w:
            if grid[r+dr][c+dc] == pattern[0] and grid[r+2*dr][c+2*dc] == pattern[1] and grid[r+3*dr][c+3*dc] == pattern[2]:
                count += 1
    return count

def part1(grid):   
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "X":
                count += count_valid_pattern(grid, r, c, "MAS")

    return count

def part2(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "A":
                count += 1 if has_valid_corners(grid, r, c) else 0

    return count

def main():
    input = open("inputs/day4.txt")
    lines = [l.strip() for l in input.readlines()]
    grid = Parser.parse_grid(lines, delim="")

    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main()