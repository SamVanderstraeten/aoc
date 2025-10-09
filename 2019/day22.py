file = open("input/day22.txt", "r")
lines = file.readlines()

size = 119315717514047
#deck = [x for x in range(size)]

tracker = 2020

results = []
for t in range(150000):
    for line in lines:
        split = line.strip().split(" ")
        num = len(split)
        if num == 2:
            c = int(split[1])
            k = c
            if c < 0:
                c = size + c
            
            #d = -1 * (size - c)
            #tempdeck = deck[d:]
            #tempdeck.extend(deck[:c])
            #deck = tempdeck[:]
            #print("CUT ", k, deck)
            tracker = tracker + (size - c) if tracker < c else tracker - c
        elif num == 4 and split[3] == "stack":
            #deck.reverse()
            #print("STACK ", deck)
            tracker = size - tracker - 1
        elif num == 4:
            #tempdeck = [x for x in range(size)]
            n = int(split[3])
            #for i in range(size):
            #    tempdeck[i*n%size] = deck[i]
            #deck = tempdeck[:]
            #print("SHUF ", n, deck)
            tracker = tracker*n%size
    if tracker in results:
        print("GOT DOUBLE")
    else:
        results.append(tracker)
    #print(tracker)