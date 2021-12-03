from aoc import lines
from collections import Counter, defaultdict

# part 1
bitcount = defaultdict(Counter)
for bits in lines("input-03.txt"):
    for position, bit in enumerate(reversed(bits)):
        bitcount[position][bit] += 1

rare, common = 0, 0
for position, counts in bitcount.items():
    if counts["1"] > counts["0"]:
        common += 2 ** position
    else:
        rare += 2 ** position

print("1:", rare * common)


# part 2
def partition(bitstrings, position):
    buckets = {"0": [], "1": []}
    for bitstring in bitstrings:
        buckets[bitstring[position]].append(bitstring)
    return buckets


common = lines("input-03.txt")
position = 0
while True:
    buckets = partition(common, position)
    if len(buckets["0"]) > len(buckets["1"]):
        common = buckets["0"]
    else:
        common = buckets["1"]
    if len(common) == 1:
        break
    position += 1

rare = lines("input-03.txt")
position = 0
while True:
    buckets = partition(rare, position)
    if len(buckets["0"]) > len(buckets["1"]):
        rare = buckets["1"]
    else:
        rare = buckets["0"]
    if len(rare) == 1:
        break
    position += 1


print("2:", int(common[0], 2) * int(rare[0], 2))
