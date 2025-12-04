from util.parser import Parser
from util.printer import Printer

def reachable(grid, x, y, max=4):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == "@":
                count += 1
    return count < max

def part1(grid):
    reach = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                if reachable(grid, r, c):
                    reach += 1    
    return reach

def part2(grid):
    removed = 0
    removed_round = -1
    while removed_round != 0:
        removed_round = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "@":
                    if reachable(grid, r, c):
                        grid[r][c] = "."
                        removed_round += 1
                        removed += 1
    return removed


def main():
    input = open("inputs/4.sam")
    lines = [l.strip() for l in input.readlines()]
    grid = Parser.parse_grid(lines, delim="")

    print("Part I: \t",part1(grid))
    print("Part II: \t",part2(grid))


if __name__ == "__main__":
    main()