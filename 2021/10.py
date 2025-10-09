file = open("input/10.sam", "r")
lines = file.readlines()

OPEN = ["[", "{", "<", "("]
CLOSER = {"[":"]","{":"}","<":">","(":")"}
SCORE = {"]":57,"}":1197,">":25137,")":3}
INC_SCORE = {"]":2,"}":3,">":4,")":1}

corrupt_score = 0
incomplete_scores = []
for line in lines:
    open = []
    for i, c in enumerate(line.strip()):
        if c in OPEN:
            open.append(c)
        else:
            last = open.pop()
            if c != CLOSER[last]:
                corrupt_score += SCORE[c]
                open = []
                break
    # Part II
    if len(open) > 0:
        open.reverse()
        closers = [CLOSER[x] for x in open]
        inc_score = 0
        for c in closers:
            inc_score = (inc_score*5) + INC_SCORE[c]
        incomplete_scores.append(inc_score)

print("Part I",corrupt_score)
incomplete_scores.sort()
print("Part II", incomplete_scores[int(len(incomplete_scores)/2)])