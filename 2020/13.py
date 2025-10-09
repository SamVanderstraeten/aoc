# Part I on paper
# Part II

#seq = [1789,37,47,1889]
#seq = [67,-1,7,59,61]
seq = [29,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,37,-1,-1,-1,-1,-1,631,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,13,19,-1,-1,-1,23,-1,-1,-1,-1,-1,-1,-1,383,-1,-1,-1,-1,-1,-1,-1,-1,-1,41,-1,-1,-1,-1,-1,-1,17]

curr_ix = 0
t = step = seq[curr_ix]

while curr_ix+1 < len(seq):
    next_ix = curr_ix + 1
    while seq[next_ix] == -1:
        next_ix += 1
    while (t+(next_ix)) % seq[next_ix] != 0:
        t += step
    step *= seq[next_ix]
    curr_ix = next_ix
print("T:",t)
    