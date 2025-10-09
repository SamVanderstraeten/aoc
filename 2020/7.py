file = open("input/7.sam", "r")
lines = file.readlines()

def find_bags_that_contain(color):
    res = []
    for line in lines:
        line = line.strip()
        splitup = line.split()
        gold_loc = line.find(color)
        if gold_loc > 0:
            res.append(splitup[0] + " " + splitup[1])
    return res

openlist = set(find_bags_that_contain("shiny gold"))
closedlist = set([e for e in openlist])
while len(openlist) > 0:
    newopen = set()
    for color in openlist:
        result = find_bags_that_contain(color)
        for r in result:
            closedlist.add(r)
            newopen.add(r)
    openlist = newopen

print(len(closedlist))

# Part II
def find_number_of_bags_for_color(color):
    total = 0
    for line in lines:
        line = line.strip().replace(",", "")
        splitup = line.split()
        cname = splitup[0] + " " + splitup[1]
        if cname == color:
            for i in range(3, len(splitup)):
                if splitup[i].isdigit():
                    c = splitup[i+1] + " " + splitup[i+2]
                    total += (int(splitup[i]) * find_number_of_bags_for_color(c))
            return (total + 1) # +1 to include the bag itself
    return (total + 1) # don't think this is ever used

number_bags = find_number_of_bags_for_color("shiny gold")
print(str(number_bags-1)) # -1 because shiny gold itself doesn'thave to be counted ("How many individual bags are required inside your single shiny gold bag?")