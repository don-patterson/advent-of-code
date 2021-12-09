from aoc import lines
from itertools import product

grid = {}
for y, row in enumerate(lines("input-09.txt")):
    for x, height in enumerate(row):
        grid[(x, y)] = int(height)


def height(x, y):
    return grid.get((x, y), 9)


def adjacent(x, y):
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]


def risk(x, y):
    for a, b in adjacent(x, y):
        if height(a, b) <= height(x, y):
            return 0
    return height(x, y) + 1


print("1:", sum(risk(x, y) for x, y in grid))

basins = [{(x, y)} for x, y in grid if risk(x, y) > 0]


def neighbors(basin):
    n = set()
    for x, y in basin:
        n.add((x, y))
        for a, b in adjacent(x, y):
            if height(x, y) < height(a, b) < 9:
                n.add((a, b))
    return n


changed = True
while changed:
    changed = False
    for basin in basins:
        n = neighbors(basin)
        if n > basin:
            basin |= n
            changed = True

largest = sorted(basins, key=len, reverse=True)
prod = 1
for basin in sorted(basins, key=len, reverse=True)[:3]:
    prod *= len(basin)
print("2:", prod)
