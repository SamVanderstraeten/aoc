file = open("input/22.sam", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

def play_game(deck_a, deck_b):
    done = False
    win = []
    game_hist = {}
    while not done:
        hash = ','.join([str(a) for a in deck_a]+["#"]+[str(b) for b in deck_b])
        if hash in game_hist:
            print("BREAK INFINITY")
            return True, deck_a
        game_hist[hash] = True

        if recurse(deck_a, deck_b):
            deck_a.append(deck_a.pop(0))
            deck_a.append(deck_b.pop(0))
        else:
            deck_b.append(deck_b.pop(0))
            deck_b.append(deck_a.pop(0))
        
        if len(deck_a) == 0:
            win = deck_b
            done = True
            return (False, win)
        if len(deck_b) == 0:
            win = deck_a
            done = True
            return (True, win)
    return win

# return true if A wins
def recurse(deck_a, deck_b, game_hist={}):
    #print("A deck:", deck_a)
    #print("B deck:", deck_b)
    
    a = deck_a[0]
    b = deck_b[0]

    #print("A picks ", a)
    #print("B picks ", b)

    if a <= len(deck_a)-1 and b <= len(deck_b)-1:
        #print("RECURSION TIME")
        #return recurse(deck_a[1:1+a], deck_b[1:1+b], game_hist)
        (a_won, result) = play_game(deck_a[1:1+a], deck_b[1:1+b])
        print("WON SUB-GAME ", "A" if a_won else "B")
        return a_won
    else:
        '''if a > b:
            print("A wins round")
        else:
            print("B wins round")'''
        return a > b

deck_a = []
deck_b = []

a = True
for line in lines[1:]:
    if line == "Player 2:":
        a = False
        continue
    if a:
        deck_a.append(int(line))
    else:
        deck_b.append(int(line))

a, win = play_game(deck_a, deck_b)

print(win)
m = 0
for i, e in enumerate(win):
    m += (len(win)-i) * e
print(m)
