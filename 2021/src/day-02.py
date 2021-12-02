from aoc import lines
from collections import Counter

# part 1
counts = Counter()
for direction, distance in lines("input-02.txt", shape=[str, int]):
    counts[direction] += int(distance)

print("1:", counts["forward"] * (counts["down"] - counts["up"]))


# part 2
counts = Counter()
for direction, distance in lines("input-02.txt", shape=[str, int]):
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
