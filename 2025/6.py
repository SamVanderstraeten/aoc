def part1(nums, ops):
    tot = 0
    for i in range(len(nums[0])):
        sum = 0 if ops[i] == '+' else 1
        for n in nums:
            if ops[i] == '+':
                sum += n[i]
            elif ops[i] == '*':
                sum *= n[i]
        tot += sum        
    return tot

def part2(input, ops):
    tr = list(zip(*input[:-1])) # SWITCH IT UP BRO (matrix transpose)
    ix = 0
    total = 0
    sum = 0 if ops[ix] == '+' else 1
    for group in tr:
        n = ''.join(group)
        if n.strip() != '':
            n = int(n)
            if ops[ix] == '+':
                sum += n
            elif ops[ix] == '*':
                sum *= n
        else:
            total += sum
            if ix+1 < len(ops):
                ix += 1
                sum = 0 if ops[ix] == '+' else 1
    return total

def main():
    input = open("inputs/6.sam").readlines()

    nums = []
    for line in input[:-1]:
        data = line.strip().split(" ")
        nums.append([int(n) for n in data if n != ''])

    ops = input[-1].strip().split(" ")
    ops = [o for o in ops if o != '']

    print("I: \t", part1(nums, ops))
    print("II: \t", part2(input, ops))

if __name__ == "__main__":
    main()