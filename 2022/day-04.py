import re

pairs = []
with open("input/04.txt") as f:
    for line in f:
        ints = [int(i) for i in re.findall("\d+", line)]
        pairs.append([[ints[0], ints[1]], [ints[2], ints[3]]])

pairs = [sorted(pair, key=lambda p: p[1] - p[0]) for pair in pairs]
print("1:", sum(1 for p1, p2 in pairs if p2[0] <= p1[0] and p2[1] >= p1[1]))

pairs = [sorted(pair) for pair in pairs]
print("2:", sum(1 for p1, p2 in pairs if p1[1] >= p2[0]))
