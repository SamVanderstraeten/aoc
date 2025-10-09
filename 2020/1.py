file = open("input/1.sam", "r")
lines = file.readlines()

nums = []
for line in lines:
    num = int(line.strip())
    
    for n in nums:
        for k in nums:
            if n+k+num == 2020:
                print(str(n*k*num))
                break    
    nums.append(num)
