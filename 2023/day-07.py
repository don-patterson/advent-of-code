from collections import Counter

hands = []
with open("input/07.txt") as f:
    for line in f:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

ranks = {
    (1,1,1,1,1): "A",
    (1,1,1,2): "B",
    (1,2,2): "C",
    (1,1,3): "D",
    (2,3): "E",
    (1,4): "F",
    (5,): "G",
    "T": "H",
    "J": "I",
    "Q": "J",
    "K": "K",
    "A": "L",
}


def order(hand):
    sig = sorted(Counter(hand).values())
    return ranks[tuple(sig)] + "".join(
        ranks.get(card, card) for card in hand
    )

hands.sort(key=lambda hand_bid: order(hand_bid[0]))
total = 0
for rank, (hand, bid) in enumerate(hands, start=1):
    total += rank * bid
print("1:", total)


ranks["J"] = "1"

def order2(hand):
    if "J" not in hand:
        return order(hand)
    
    counts = Counter(hand)
    J = counts["J"]
    del counts["J"]
    counts = [1]*J + sorted(counts.values())
    sig = ranks[tuple(counts)]
    for _ in range(J):
        sig = wild[sig]
    return sig + "".join(
        ranks.get(card, card) for card in hand
    )

wild = {
    "A": "B",
    "B": "D",
    "C": "E",
    "D": "F",
    # "E":... can't have a full house + joker
    "F": "G",
    "G": "G", # can't really have this except JJJJJ edge case..
}

hands.sort(key=lambda hand_bid: order2(hand_bid[0]))
total = 0
for rank, (hand, bid) in enumerate(hands, start=1):
    total += rank * bid
print("2:", total)