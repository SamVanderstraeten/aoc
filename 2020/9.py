file = open("input/9.sam", "r")
lines = file.readlines()

def find_invalid(nums, preamble=25):
    for i in range(preamble, len(nums)):
        sum = nums[i]
        sumok = False
        for x in nums[i-preamble:i]:
            for y in nums[i-preamble:i]:
                if x+y == sum:
                    sumok = True
        if not sumok:
            return sum

def find_sum_combo(nums, sum):
    for x in range(0, len(nums)):
        t = nums[x]
        for y in range(x+1, len(nums)):
            t += nums[y]
            if t == sum:
                return min(nums[x:y]) + max(nums[x:y])
            elif t > sum:
                break

nums = [int(x) for x in lines]
inv = find_invalid(nums)
print("Invalid",inv)
combo = find_sum_combo(nums, inv)
print("Combo",combo)