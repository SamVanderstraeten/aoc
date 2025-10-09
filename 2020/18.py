file = open("input/18.sam", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

def solve2(line):
    result = 0
    sign = "+"
    i = 0
    while i < len(line):
        c = line[i]
        if c.isnumeric():
            if sign == "+":
                result += int(c)
            if sign == "*":
                result *= solve2(line[i:])
                return result
        elif c == "+":
            sign = "+"
        elif c == "*":
            sign = "*"
        elif c == "(":
            if sign == "*":
                result *= solve2(line[i:])
                return result
            open = 0
            end = i
            for j in range(i+1, len(line)):
                if line[j] == ")":
                    if open == 0:
                        end = j
                    else:
                        open -= 1
                elif line[j] == "(":
                    open += 1
            sub = line[i+1:end]
            if sign == "+":
                result += solve2(sub)
            if sign == "*":
                result *= solve2(sub)
            i = end
        i+=1
    return result

def solve(line):
    result = 0

    sign = "+"
    i = 0
    while i < len(line):
        c = line[i]
        if c.isnumeric():
            if sign == "+":
                result += int(c)
            if sign == "*":
                result *= int(c)
        elif c == "+":
            sign = "+"
        elif c == "*":
            sign = "*"
        elif c == "(":
            open = 0
            end = i
            for j in range(i+1, len(line)):
                if line[j] == ")":
                    if open == 0:
                        end = j
                    else:
                        open -= 1
                elif line[j] == "(":
                    open += 1
            sub = line[i+1:end]
            if sign == "+":
                result += solve(sub)
            if sign == "*":
                result *= solve(sub)
            i = end
        i+=1
    return result

result1 = 0
result2 = 0
for line in lines:
    result1 += solve(line)
    result2 += solve2(line)
print("Part 1:",result1)
print("Part 2:",result2)