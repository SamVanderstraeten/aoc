file = open("input/2.sam", "r")
lines = [l.strip() for l in file.readlines()]

class Game:
    def __init__(self, str) -> None:
        self.str = str
        self.parse()

    # I feel dirty
    def parse(self):
        data = self.str.split(": ")
        self.id = data[0].split()[1]
        self.grabs = [x for x in data[1].split("; ")]
        self.all_grabs = []
        for n in [x.split(",") for x in self.grabs]:
            p = [0,0,0]
            for k in n:
                s = k.split()
                if s[1] == "red":
                    p[0] = int(s[0])
                elif s[1] == "green":
                    p[1] = int(s[0])
                elif s[1] == "blue":
                    p[2] = int(s[0])
            self.all_grabs.append(p)

    def valid(self):
        for g in self.all_grabs:
            if not self.valid_grab(g):
                return False 
        return True   
            
    def valid_grab(self, g):
        return g[0] <= 12 and g[1] <= 13 and g[2] <= 14
    
    def power(self):
        mx = [max(x) for x in zip(*self.all_grabs)]
        return mx[0] * mx[1] * mx[2]

# Init games
games = [Game(x) for x in lines]

# Determine valid games
valid = [int(x.id) for x in games if x.valid()]
print("Part I:", sum(valid))

# Calculate powers
powers = [x.power() for x in games]
print("Part II:",sum(powers))