file = open("input/4.sam", "r")
lines = file.readlines()

boards = []

# Parsing the boards
input = [int(n) for n in lines.pop(0).split(",")]
for line in lines:
    if line == "\n":
        boards.append([])
        continue
    numbers = [int(n) for n in line.strip().split()]
    boards[-1].append(numbers)

winner = loser = None
for board in boards:
    # Determine rounds of input that it takes to complete board, keep track of best and worst board
    board_wins_at = len(input)
    # rows
    for row in board:
        row_turns = max([input.index(n) for n in row])
        board_wins_at = min(row_turns, board_wins_at)
    #cols
    for i in range(0, len(boards[0])):
        col = [r[i] for r in board]
        col_turns = max([input.index(n) for n in col])
        board_wins_at = min(col_turns, board_wins_at)

    #Part I - winner
    if winner == None or winner[0] > board_wins_at:
        closed_numbers = input[:board_wins_at+1]
        open_numbers_sum = 0
        for row in board:
            open_numbers_sum += sum([n for n in row if not n in closed_numbers])
        winner = (board_wins_at, input[board_wins_at]*open_numbers_sum)

    #Part II - worst
    if loser == None or loser[0] < board_wins_at:
        closed_numbers = input[:board_wins_at+1]
        open_numbers_sum = 0
        for row in board:
            open_numbers_sum += sum([n for n in row if not n in closed_numbers])
        loser = (board_wins_at, input[board_wins_at]*open_numbers_sum)

print("Winner:", winner[1])
print("Worst:", loser[1])