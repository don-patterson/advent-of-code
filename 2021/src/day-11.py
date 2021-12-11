from aoc import lines
from itertools import product

grid = {}
for y, row in enumerate(lines("input-11.txt")):
    for x, value in enumerate(row):
        grid[(x, y)] = int(value)

near = set(product((-1, 0, 1), repeat=2)) - {(0, 0)}


def adjacent(x, y):
    return {(x + i, y + j) for i, j in near} & grid.keys()


def increment(x, y):
    grid[(x, y)] += 1
    if grid[(x, y)] == 10:
        for a, b in adjacent(x, y):
            increment(a, b)


def step():
    flashes = 0
    for (x, y) in grid:
        increment(x, y)
    for (x, y) in grid:
        if grid[(x, y)] >= 10:
            flashes += 1
            grid[(x, y)] = 0
    return flashes


print("1:", sum(step() for _ in range(100)))

n = len(grid)
steps = 1
while step() != n:
    steps += 1
print("2:", steps + 100)
