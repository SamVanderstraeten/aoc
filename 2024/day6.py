from util.parser import Parser
from util.printer import Printer

def turn_right(D):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L
    new_dir = (D + 1) % 4
    return new_dir, dirs[new_dir]

def next(grid, pos, dir):
    nx = pos[0] + dir[0]
    ny = pos[1] + dir[1]

    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
        return grid[nx][ny]
    return "$"  # Out of bounds

def move_fwd(pos, dir):
    x, y = pos
    dx, dy = dir
    return (x + dx, y + dy)

def visit(grid, pos):
    r, c = pos
    grid[r][c] = "X"

def store(db, pos, dir):
    db_key = (pos)
    db_value = dir
    if db_key not in db:
        db[db_key] = db_value

def already_visited(db, pos, dir):
    db_key = (pos)
    db_value = dir
    return db_key in db and db[db_key] == db_value

def part1(g, start):
    grid = [row.copy() for row in g]
    D = -1 # start -1 so first turn_right goes to 0 (up)
    D, dir = turn_right(D)
    pos = start

    while True:
        while next(grid, pos, dir) in ".X^":
            pos = move_fwd(pos, dir)
            visit(grid, pos)

        if next(grid, pos, dir) != "#":
            break
        D, dir = turn_right(D)
    
    return sum([row.count("X") for row in grid])

def part2(g, start):
    loop_count = 0

    for r in range(len(g)):
        print(f"Row {r}/{len(g)}")
        for c in range(len(g[0])):
            db = {}
            if g[r][c] == "#" or g[r][c] == "^":
                continue
            grid = [row.copy() for row in g]
            grid[r][c] = "#"
            D = -1 # start -1 so first turn_right goes to 0 (up)
            D, dir = turn_right(D)
            pos = start
            
            while True:
                pl = loop_count
                while next(grid, pos, dir) in ".X^": # move straight forward in [dir] as far as possible
                    pos = move_fwd(pos, dir)
                    if already_visited(db, pos, dir):
                        loop_count += 1
                        break
                    else:
                        store(db, pos, dir)

                if pl != loop_count: # loop found, break
                    break

                if next(grid, pos, dir) == "$": # hit end of path
                    break

                D, dir = turn_right(D)
    
    return loop_count

def main():
    input = open("inputs/day6.txt")
    lines = [l.strip() for l in input.readlines()]
    grid = Parser.parse_grid(lines, delim="")

    start = (0,0)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "^":
                start = (r,c)

    print(part1(grid, start))
    print(part2(grid, start))

if __name__ == "__main__":
    main()