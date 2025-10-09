import itertools
player_pos=[6,4]
player_score = [0,0]

dice = -1
def next_dice_num():
    global dice
    dice = (dice+1)%100
    return dice+1

def dice_roll():
    return [next_dice_num(),next_dice_num(),next_dice_num()]
    
die_rolls = 0
while max(player_score) < 1000:
    p1=dice_roll()
    die_rolls+=1
    player_pos[0] = ((player_pos[0]+sum(p1))%10)
    if player_pos[0] == 0:
        player_pos[0] = 10
    player_score[0]+=player_pos[0]

    if player_score[0] >= 1000:
        break

    p2=dice_roll()
    die_rolls+=1
    player_pos[1] = ((player_pos[1]+sum(p2))%10)
    if player_pos[1] == 0:
        player_pos[1] = 10
    player_score[1]+=player_pos[1]
print("Part I",min(player_score[0],player_score[1])*die_rolls*3)

outcomes={}
def game(pos1,pos2,score1=0,score2=0,turn=0):
    global outcomes
    if (pos1,pos2,score1,score2,turn) in outcomes:
        return outcomes[(pos1,pos2,score1,score2,turn)]
    winner = [0,0]
    pms = list(set(itertools.permutations([1, 2, 3]*3,3)))
    for p in pms:
        pos = [pos1,pos2]
        score = [score1,score2]
        roll = sum(p)
        pos[turn] = ((pos[turn]+roll)%10)
        if pos[turn] == 0:
            pos[turn] = 10
        score[turn]+=pos[turn]
        if score[turn] >= 21:
            winner[turn] += 1
        else:
            sub_winners = game(pos[0],pos[1],score[0],score[1], (turn+1)%2)
            winner[0] += sub_winners[0]
            winner[1] += sub_winners[1]

    outcomes[(pos1,pos2,score1,score2,turn)] = winner
    return winner
print("Part II",max(game(player_pos[0], player_pos[1])))