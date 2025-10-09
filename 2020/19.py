file = open("input/19c.sam", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

rules = {}
parsing = True
count = 0

def check_msg(line, r='0', cursor=0):
    print("checking",line,cursor)
    rule = rules[r]
    orig_cursor = cursor
    if cursor >= len(line):
        print(">>> end reached OK")
        return True, cursor
    for sub in rule:
        print("SUB",sub)
        valid = True
        cursor = orig_cursor
        for k in sub:
            print(k)
            if k.isalpha():
                if line[cursor] != k:
                    valid = False
                    break
                cursor += 1
            else:
                v, l = check_msg(line, k, cursor)
                if not v:
                    valid = False
                    break
                else:
                    cursor = l
        if valid:
            print("SUB VALID!",sub,cursor)
            return True, cursor
        else:
            print("SUB NOT valid",sub,cursor)
    return False, 0
        
for i, line in enumerate(lines):
    if line == "":
        parsing = False
        continue
    if parsing:
        ix, rule = line.split(": ")
        subs = [[k.replace('"', '') for k in r.strip().split(" ")] for r in rule.split("|")]
        rules[ix] = subs
    else:
        v, b = check_msg(line)
        if v and b == len(line):
            print("###",line,"is valid")
            count += 1
        else:
            print("###",line,"is not valid")
        
print("Total valid: ",count)