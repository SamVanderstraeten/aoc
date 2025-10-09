def part1(reports):
    safe = 0
    for report in reports:
        if check_report(report):
            safe += 1

    return safe

def part2(reports):
    safe = 0
    for report in reports:
        safe_variant = False
        for i in range(len(report)):
            stop = i
            start = i + 1
            r = report[:stop] + report[start:]
            if check_report(r):
                safe_variant = True
                break
        if safe_variant:
            safe += 1
    return safe

def check_report(report):
    diffs = [report[x]-report[x-1] for x in range(1,len(report))]
    zero = 0 in diffs
    above_zero = [x for x in diffs if x > 0]
    
    return not zero and (len(above_zero) == 0 or len(above_zero) == len(diffs)) and max([abs(x) for x in diffs]) < 4

def main():
    input = open("inputs/day2.txt").read().strip()
    reports = [list(map(int, x.split(" "))) for x in input.splitlines()]

    print(part1(reports))
    print(part2(reports))


if __name__ == "__main__":
    main()