def part1(ranges, ingredients):
    sum = 0

    for i in ingredients:
        ii = int(i)
        for r in ranges:
            low, high = map(int, r)
            if low <= ii <= high:
                sum += 1
                break
            

    return sum

def part2(ranges):
    sum=0
    merged_ranges = []

    # Merge overlapping ranges
    for r in ranges:
        current_low, current_high = map(int, r)
        if not merged_ranges:
            merged_ranges.append([current_low, current_high])
            continue

        remove_indexes = []
        for ix, m in enumerate(merged_ranges):
            m_low, m_high = map(int, m)
            if m_low <= current_low <= m_high and current_high > m_high: # overlap, extend high
                current_low = m_low
                remove_indexes.append(ix)
            elif m_low <= current_high <= m_high and current_low < m_low: # overlap, extend low
                current_high = m_high
                remove_indexes.append(ix)
            elif current_low <= m_low and current_high >= m_high: # current eats m, replace
                remove_indexes.append(ix)
            elif m_low <= current_low and m_high >= current_high: # m eats current, throw it away
                current_low = None
                current_high = None
                break

        # Append the definitive range if it wasn't eaten
        if current_low is not None and current_high is not None:
            merged_ranges.append([current_low, current_high])

        # Remove all ranges that have been merged in the definitive range
        for ix in sorted(remove_indexes, reverse=True):
            merged_ranges.pop(ix)

    for m in merged_ranges:
        sum += m[1] - m[0] + 1

    return sum

def main():
    input = open("inputs/5.sam").read().strip()
    ranges, ingredients = input.split("\n\n")
    
    ingredients = ingredients.split("\n")
    ranges = [r.split("-") for r in ranges.split("\n")]

    print("I: \t", part1(ranges, ingredients))
    print("II: \t", part2(ranges))

if __name__ == "__main__":
    main()