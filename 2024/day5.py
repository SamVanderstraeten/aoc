def part1(updates, rules):
    count = 0
    invalid = []
    for update in updates:
        done = []
        valid = True
        for page in update:
            if page in rules:
                req = rules[page]
                for r in req:
                    if r in done:
                        valid = False
            done.append(page)
        if valid == True:
            count += update[len(update)//2]   
        else:
            invalid.append(update)     
    return invalid, count

def part2(invalid_updates, rules):
    # Reorder numbers in updates to satisfy rules
    for update in invalid_updates:
        print("> ", update)
        done = []
        i=0
        while i < len(update):
            swapped = False
            page = update[i]
            if page in rules:
                req = rules[page]
                for r in req:
                    if r in done:                        
                        # Swap r and page in update
                        idx = update.index(r)
                        update[idx], update[i] = update[i], update[idx]
                        i = 0
                        done = []
                        swapped = True
                        break
            if not swapped:
                done.append(page)
                i+=1

    # Calculate the sum of the middle pages
    count = 0
    for update in invalid_updates:
        count += update[len(update)//2]

    return count

def main():
    input = open("inputs/day5.txt").read().strip()
    (rules_raw, updates) = input.split("\n\n")

    updates = [[int(x) for x in line.split(",")] for line in updates.split("\n")]
    rules = {}
    for rule in rules_raw.split("\n"):
        (pre, post) = rule.split("|")
        (pre, post) = (int(pre), int(post))
        if pre not in rules:
            rules[pre] = []
        rules[pre].append(post)     

    invalid, count = part1(updates, rules)
    print(count)
    print(part2(invalid, rules))

if __name__ == "__main__":
    main()