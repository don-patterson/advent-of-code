from aoc import lines

positions = []
for line in lines("input-07.txt"):
    positions.extend(int(i) for i in line.split(","))


def cost1(a, b):
    return abs(a - b)


def cost2(a, b):
    diff = cost1(a, b)
    return int((diff * (diff + 1)) / 2)


min_cost1 = None
min_cost2 = None
for p in range(min(positions), max(positions)):
    c1 = sum(cost1(p, i) for i in positions)
    c2 = sum(cost2(p, i) for i in positions)
    if min_cost1 is None or c1 < min_cost1:
        min_cost1 = c1
    if min_cost2 is None or c2 < min_cost2:
        min_cost2 = c2

print("1:", min_cost1)
print("2:", min_cost2)
