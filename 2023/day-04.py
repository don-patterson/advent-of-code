cards = []
with open("input/04.txt") as f:
    for line in f:
        for thing in line.split():
            if thing == "Card":
                continue
            elif thing.endswith(":"):
                cards.append({"win":[], "have":[]})
                target = cards[-1]["win"]
            elif thing == "|":
                target = cards[-1]["have"]
            else:
                target.append(int(thing))

def score(card):
    matches = sum(1 for have in card["have"] if have in card["win"])
    return int(pow(2, matches-1))

print("1:", sum(score(card) for card in cards))

i = len(cards)-1
while i >= 0:
    matches = sum(1 for have in cards[i]["have"] if have in cards[i]["win"])
    count = 1
    for j in range(matches):
        count += cards[i+j+1]
    cards[i] = count
    i -= 1

print("2:", sum(cards))
