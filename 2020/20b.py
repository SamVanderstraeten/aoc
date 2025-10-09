import numpy

file = open("input/20b.sam", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

class Tile:
    def __init__(self, id, grid) -> None:
        self.id = id
        self.grid = grid


i = 0
while i < len(lines):
    line = lines[i]
    t, tile_id = line[:-1].split(" ")
    if t == "Tile":
        tile = lines[i+1:i+11]
        i += 11
