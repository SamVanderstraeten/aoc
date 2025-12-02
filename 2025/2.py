def part1(ranges):
    sum = 0

    for a, b in ranges:
        for i in range(a, b + 1):
            str_i = str(i)
            if(len(str_i) % 2 == 0):
                if str_i[:(len(str_i)//2)] == str_i[len(str_i)//2:]:
                    sum += i                 

    return sum

def part2(ranges):
    sum = 0
    lastfound = ""
    for a, b in ranges:
        for i in range(a, b + 1):
            str_i = str(i)

            for deler in range(2, len(str_i)+1):
                if(len(str_i) % deler == 0):

                    chunks = []
                    size = len(str_i) // deler
                    for _ in range(deler):
                        chunk = str_i[_ * size: (_ + 1) * size]
                        if any(x != chunk for x in chunks):
                            break
                        chunks.append(chunk)

                    if len(chunks) == deler:
                        if lastfound != str_i: # prevent double counting
                            lastfound = str_i
                            sum += i

    return sum

def main():
    input = open("inputs/2.sam").read().strip()
    ranges = [r.split("-") for r in input.split(",")]
    ranges = [(int(a), int(b)) for a, b in ranges]
    print(ranges)
    
    print("I: \t", part1(ranges))
    print("II: \t", part2(ranges))

if __name__ == "__main__":
    main()