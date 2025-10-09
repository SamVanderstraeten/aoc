file = open("input/1.sam", "r")
lines = file.readlines()
nums = [int(n) for n in lines]

# Part I + fill list for part II
c = 0
for n in range(1, len(nums)):
    if nums[n-1] < nums[n]:
        c+=1
print(c)

# Part II
c = 0
for n in range(0, len(nums)-2):
    sw1 = sum(nums[n:n+3])
    sw2 = sum(nums[n+1:n+4])
    if sw2 > sw1:
        c+=1
print(c)