file = open("input/22.sam", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

deck_a = []
deck_b = []
ix_a = 0
ix_b = 0
off_a = []
off_b = []

a = True
for line in lines[1:]:
    if line == "Player 2:":
        a = False
        continue
    if a:
        deck_a.append(int(line))
    else:
        deck_b.append(int(line))

done = False
win = []
while not done:
    if deck_a[ix_a] > deck_b[ix_b]:
        off_a.append(deck_a[ix_a])
        off_a.append(deck_b[ix_b])
    else:
        off_b.append(deck_b[ix_b])
        off_b.append(deck_a[ix_a])

    ix_a = (ix_a + 1) if (ix_a + 1) < len(deck_a) else 0
    ix_b = (ix_b + 1) if (ix_b + 1) < len(deck_b) else 0

    if ix_a == 0:
        deck_a = off_a
        off_a = []
        if len(deck_a) == 0:
            win = deck_b[ix_b:] + off_b
            done = True
    if ix_b == 0:
        deck_b = off_b
        off_b = []
        if len(deck_b) == 0:
            win = deck_a[ix_a:] + off_a
            done = True
print(win)

m = 0
for i, e in enumerate(win):
    m += (len(win)-i) * e
print(m)
