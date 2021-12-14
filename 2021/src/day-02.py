from collections import Counter


def input():
    with open("input-02.txt") as text:
        for line in text:
            direction, distance = line.split()
            yield direction, int(distance)


# part 1
counts = Counter()
for direction, distance in input():
    counts[direction] += distance

print("1:", counts["forward"] * (counts["down"] - counts["up"]))


# part 2
counts = Counter()
for direction, distance in input():
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
