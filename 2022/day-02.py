r = "rock"
p = "paper"
s = "scissors"

move_score = {r: 1, p: 2, s: 3}
left_win = {(r, s), (s, p), (p, r)}
move = {"A": r, "B": p, "C": s, "X": r, "Y": p, "Z": s}

with open("input/02.txt") as f:
    moves = [(move[line[0]], move[line[2]]) for line in f]

score = 0
for opp, mine in moves:
    score += move_score[mine]
    if (opp, mine) in left_win:
        continue
    if (mine, opp) in left_win:
        score += 6
        continue
    score += 3

print("1:", score)


def win(opp):
    for left, right in left_win:
        if opp == right:
            return left


def lose(opp):
    for left, right in left_win:
        if opp == left:
            return right


def tie(opp):
    return opp


outcome_map = {r: lose, p: tie, s: win}

score = 0
for opp, outcome_key in moves:
    outcome = outcome_map[outcome_key]
    if outcome == win:
        score += 6
    elif outcome == tie:
        score += 3
    score += move_score[outcome(opp)]

print("2:", score)
# I feel like this whole thing could be done in 10 lines, but oh well
