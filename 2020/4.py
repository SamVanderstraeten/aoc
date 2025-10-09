file = open("input/4.sam", "r")
lines = file.readlines()

def is_valid(k,v):
    if k == "byr":
        if 1920 <= int(v) <= 2002:
            return True
    elif k == "iyr":
        if 2010 <= int(v) <= 2020:
            return True
    elif k == "eyr":
        if 2020 <= int(v) <= 2030:
            return True 
    elif k == "hgt":
        unit = v[-2:]
        if unit == "cm":
            if 150 <= int(v[:-2]) <= 193:
                return True 
        elif unit == "in":
            if 59 <= int(v[:-2]) <= 76:
                return True 
    elif k == "hcl":
        if len(v) == 7 and v[0] == "#":
            return True
    elif k == "ecl":
        if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    elif k == "pid":
        if len(v) == 9 and v.isnumeric():
            return True
    elif k == "cid":
        return True

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

current_passport = []
valid = 0
for line in lines:
    line = line.strip()
    if line == "":
        if all(elem in current_passport for elem in required):
            valid += 1
        current_passport = []
        continue

    for entry in line.split():
        (k,v) = entry.split(":")
        if is_valid(k,v): # Part II = this if-statement
            current_passport.append(k)

print(str(valid))