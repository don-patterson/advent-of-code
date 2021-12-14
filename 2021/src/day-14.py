from collections import Counter
from itertools import pairwise


def input():
    with open("input-14.txt") as lines:
        for line in lines:
            yield line.strip()


lines = input()
sequence = [a + b for a, b in pairwise(next(lines))]
next(lines)  # blank
insertions = {}
for line in lines:
    pair, c = line.split(" -> ")
    insertions[pair] = c

pairs = Counter(sequence)


def step(current):
    updated = Counter()
    for pair, count in current.items():
        if pair in insertions:
            c = insertions[pair]
            updated[pair[0] + c] += count
            updated[c + pair[1]] += count
        else:
            updated[pair] += count
    return updated


def count(pairs):
    # the leftmost and rightmost characters in the sequence are not double counted,
    # and all others are..so I got lucky that the most/least common were double counted
    c = Counter()
    for pair, count in pairs.items():
        c[pair[0]] += count
        c[pair[1]] += count
    [most, *_, least] = c.most_common()
    return (most[1] - least[1]) // 2


for _ in range(10):
    pairs = step(pairs)
print("1:", count(pairs))

for _ in range(30):
    pairs = step(pairs)
print("2:", count(pairs))
