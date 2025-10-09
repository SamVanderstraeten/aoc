file = open("input/10c.sam", "r")
lines = file.readlines()

nums = [int(x) for x in lines]
nums.insert(0,0)
nums.append(max(nums) + 3)
nums.sort()

ones = 0
threes = 0
for i in range(1, len(nums)):
    num = nums[i]
    prenum = nums[i-1]
    if num - prenum == 1:
        ones+=1
    if num - prenum == 3:
        threes+=1

print(str(ones*threes))

# Part II
combobreaker = {0: 1}
for i in range(0, len(nums)):
    j = i + 1
    while j < len(nums) and nums[j] - nums[i] <= 3:
        if not j in combobreaker:
            combobreaker[j] = 0
        combobreaker[j] += combobreaker[i]
        j += 1
print(combobreaker)
print(combobreaker[len(nums)-1])
