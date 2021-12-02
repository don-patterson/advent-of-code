from aoc_common import load_lines
from collections import Counter

input = load_lines("input-02.txt")

# part 1
counts = Counter()
for line in input:
    direction, distance = line.split()
    counts[direction] += int(distance)

print("1:", counts["forward"] * (counts["down"] - counts["up"]))

# part 2
counts = Counter()
for line in input:
    direction, distance = line.split()
    distance = int(distance)

    if direction == "up":
        counts["aim"] -= distance
    elif direction == "down":
        counts["aim"] += distance
    elif direction == "forward":
        counts["position"] += distance
        counts["depth"] += counts["aim"] * distance
    else:
        print("uh oh!")

print("2:", counts["position"] * counts["depth"])
