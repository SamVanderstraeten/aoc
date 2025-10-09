file = open("input/3.sam", "r")
lines = file.readlines()

# Part I
decimals = [int(x, 2) for x in lines]
prevp = pow(2, len(lines[0]))
gamma = ""
for i in range(0,len(lines[0])-1):
    p = pow(2, len(lines[0])-2-i)
    larger = [x for x in decimals if ((x%prevp) >= p)]
    smaller = [x for x in decimals if ((x%prevp) < p)]
    gamma += "1" if len(larger) >= len(smaller) else "0"
    prevp = p
eps = ["1" if x == "0" else "0" for x in gamma]
print(int(gamma, 2) * int("".join(eps), 2))


#Part II
def follow_bit_count(decimals, prevp, most_common=True):
    for i in range(0,len(lines[0])-1):
        p = pow(2, len(lines[0])-2-i)
        larger = [x for x in decimals if ((x%prevp) >= p)]
        smaller = [x for x in decimals if ((x%prevp) < p)]
        if most_common:
            decimals = larger if len(larger) >= len(smaller) else smaller
        else:
            decimals = smaller if len(smaller) <= len(larger) else larger
        prevp = p
        if len(decimals) == 1:
            return decimals[0]


numbers = [int(x, 2) for x in lines]
start_p = pow(2, len(lines[0])) # larger than biggest number in list

oxy = follow_bit_count(decimals, start_p)
co2 = follow_bit_count(decimals, start_p, False)

print(oxy*co2)