file = open("input/8.sam", "r")
lines = file.readlines()

count = 0
for line in [x.strip().split(" | ")[1] for x in lines]:
    for n in line.split(" "):
        length = len(n)
        if length == 2 or length == 7 or length == 4 or length == 3:
            count += 1
print("Part I: ",count)

def find_length(list, n):
    return [x for x in list if len(x) == n]

def diff(str, str2):
    return [x for x in str2 if str.find(x) == -1]

tot = 0
for line, number in [x.strip().split(" | ") for x in lines]:
    leds = [''.join(sorted(x)) for x in line.split(" ")]
    map = {}
    map[1] = find_length(leds, 2)[0]
    map[7] = find_length(leds, 3)[0]
    map[4] = find_length(leds, 4)[0]
    map[8] = find_length(leds, 7)[0]

    seg6 = find_length(leds, 6) # 6 segments: numbers 6, 9 & 0
    for seg in seg6:
        if len(diff(seg, map[7])) == 1:
            map[6] = seg
        elif len(diff(seg, map[4])) == 0:
            map[9] = seg
        else:
            map[0] = seg

    seg5 = find_length(leds, 5) # 5 segments: numbers 2, 3 & 5
    for seg in seg5:
        if len(diff(seg, map[7])) == 0:
            map[3] = seg
        elif len(diff(seg, map[6])) == 1:
            map[5] = seg
        else:
            map[2] = seg 

    inv_map = {v: k for k, v in map.items()}
    ns = int(''.join([str(inv_map[''.join(sorted(n))]) for n in number.split(" ")]))
    tot += ns
print("Part II ",tot)