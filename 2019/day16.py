import sys, math

file = open("input/day16.txt", "r")
lines = file.readlines()

seq = [int(c) for c in str(lines[0])]
original = seq[:]

pattern = [0, 1, 0, -1]

steps = 100
count = len(seq)
for x in range(steps):
    orig = seq[:]

    for i in range(count):
        size = i + 1
        tot = 0

        j = i
        while j < count:
            tot += sum(orig[j:j + size])
            j += 2 * size

            tot -= sum(orig[j:j + size])
            j += 2 * size

        seq[i] = abs(tot) % 10

print("Part 1: " + "".join([str(x) for x in seq])[:8])

# part 2
# first 7 digits = skip a lot of numbers
skippers = int(''.join([str(x) for x in original[:7]]))
nums = (original * 10000)[skippers:]
count = len(nums)

for step in range(100):
    for i in range(count - 2, -1, -1): # loop backwards
        nums[i] += nums[i + 1]
        nums[i] %= 10

print("Part 2: " + "".join([str(x) for x in nums[:8]]))