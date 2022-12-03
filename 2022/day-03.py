from string import ascii_letters
from itertools import islice

with open("input/03.txt") as f:
    rucksacks = f.read().splitlines()


def priority(letter):
    return ascii_letters.index(letter) + 1


total_priority = 0
for r in rucksacks:
    mid = len(r) // 2
    overlap = set(r[:mid]) & set(r[mid:])
    total_priority += priority(overlap.pop())
print("1:", total_priority)

total_priority = 0
groups = iter(rucksacks)
while group := list(islice(groups, 3)):
    total_priority += priority(set.intersection(*[set(r) for r in group]).pop())
print("2:", total_priority)
