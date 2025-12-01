def part1(operations):
    dial = 50
    c = 0
    for op in operations:
        if op[0] == "L":
            dial = (dial - int(op[1:])) % 100
        elif op[0] == "R":
            dial = (dial + int(op[1:])) % 100
        if dial == 0:
            c+=1
    return c

def part2(operations):
    dial = 50
    c = 0
    for op in operations:
        if op[0] == "L":
            new_val = (dial - int(op[1:]))
        elif op[0] == "R":
            new_val = (dial + int(op[1:]))
        
        if new_val < 0:
            c += abs(new_val) // 100 + (0 if dial == 0 else 1)    
        elif new_val >= 100:
            c += new_val // 100 
        elif new_val == 0:
            c += 1
        
        dial = new_val % 100
    return c

def main():
    input = open("inputs/1.sam").read().strip()
    operations = [line for line in input.split("\n")]
    
    print("I: \t", part1(operations))
    print("II: \t", part2(operations))

if __name__ == "__main__":
    main()