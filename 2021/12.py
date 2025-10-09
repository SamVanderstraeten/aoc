file = open("input/12.sam", "r")
lines = file.readlines()

# Preprocess graph
graph = {}
def add_to_graph(a,b):
    if b != "start":
        if a in graph.keys():
            graph[a].append(b)
        else:
            graph[a] = [b]

for line in lines:
    a,b = line.strip().split("-")
    add_to_graph(a,b)
    add_to_graph(b,a)

def has_double_visited(path):
    return any([n[0].islower() for n in set([x for x in path if path.count(x) > 1])])

def generate(paths, part2=False):
    if all([path[-1] == "end" for path in paths]):
        return paths
    result = []
    for path in paths:
        loc = path[-1]
        if loc != "end":
            for node in graph[loc]:
                if node[0].isupper() or not node in path or (part2 and node in path and not has_double_visited(path)):
                    p = path.copy()
                    p.append(node)
                    result.append(p)
        else:
            result.append(path)
    return generate(result, part2)

print("Part I",len(generate([["start"]])))
print("Part II",len(generate([["start"]], True)))