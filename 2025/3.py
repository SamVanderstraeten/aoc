def find_max(numstr):
    m = max([int(n) for n in numstr])
    max_index = numstr.index(str(m))
    return m, max_index

def part1(batteries):
    sum = 0

    for battery in batteries:                  
        first_max, max_index = find_max(battery[:-1])
        second_max, max_index = find_max(battery[max_index+1:])
        power = int(str(first_max) + str(second_max))
        sum += power

    return sum

def part2(batteries):
    sum = 0
    size = 12

    for battery in batteries:          
        position = 0   
        power = ""    
        for _ in range(size):
            offset = -1 * (size-1-_)
            if offset == 0:
                offset = None
            m, max_index = find_max(battery[position:offset])
            position += max_index + 1
            power += str(m)
    
        sum += int(power)

    return sum

def main():
    input = open("inputs/3.sam").readlines()
    batteries = [n.strip() for n in input]
    
    print("I: \t", part1(batteries))
    print("II: \t", part2(batteries))

if __name__ == "__main__":
    main()