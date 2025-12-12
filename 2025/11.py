from collections import deque

from functools import lru_cache

def dfs2(graph, start, end, must_include=[None, None]):
    a, b = must_include

    @lru_cache(maxsize=None)
    def dp(node, seen):  # seen is (seen_a, seen_b)
        seen_a, seen_b = seen

        if node == end:
            ok_a = True if a is None else seen_a
            ok_b = True if b is None else seen_b
            return 1 if (ok_a and ok_b) else 0

        total = 0
        for neighbor in graph.get(node, []):
            total += dp(neighbor, (
                seen_a or (a is not None and neighbor == a),
                seen_b or (b is not None and neighbor == b),
            ))
        return total

    start_seen = (
        (a is not None and start == a),
        (b is not None and start == b),
    )
    return dp(start, start_seen)

# Depth-first search time
def dfs(graph, start, end):
    queue = deque()
    queue.append( (start, set([start])) )

    count = 0

    while queue:
        node, visited = queue.pop()
        if node == end:
            count += 1
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    queue.append( (neighbor, new_visited) )
    return count

def part1(data):
    return dfs(data, 'you', 'out')

def part2(data):
    return dfs2(data, 'svr', 'out', ['dac', 'fft'])

def main():
    input = open("inputs/11.sam").readlines()

    lines = {}
    for line in input:
        d = line.split(": ")
        lines[d[0]] = d[1].strip().split(" ")

    print("I: \t", part1(lines))
    print("II: \t", part2(lines))

if __name__ == "__main__":
    main()