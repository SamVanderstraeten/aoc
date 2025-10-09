file = open("input/2.sam", "r")
lines = file.readlines()

valid = 0
for line in lines:
    (policy, passphrase) = line.strip().split(":")
    (minmax, letter) = policy.split()
    (min, max) = minmax.split("-")
    (min, max) = (int(min), int(max))
    passphrase = passphrase.strip()

    # PART II
    count = 0
    if passphrase[min-1] == letter:
        count += 1
    if passphrase[max-1] == letter:
        count += 1
    if count == 1:
        valid += 1

    '''
    # PART I
    count = 0
    for l in passphrase:
        if l == letter:
            count+=1
        
    if min <= count and count <= max:
        valid += 1
    '''

print(str(valid))