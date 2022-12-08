from math import prod

grid = {}
with open("input/08.txt") as f:
    for y, row in enumerate(f):
        for x, h in enumerate(row.strip()):
            grid[(x, y)] = int(h)

directions = ((-1, 0), (1, 0), (0, 1), (0, -1))


def ray(start, direction):
    x, y = start
    step_x, step_y = direction
    while (x := x + step_x, y := y + step_y) in grid:
        yield x, y


def visible(start):
    return any(all(grid[p] < grid[start] for p in ray(start, d)) for d in directions)


print("1:", sum(1 for p in grid if visible(p)))


def view(start, direction):
    for p in ray(start, direction):
        yield 1
        if grid[p] >= grid[start]:
            break


def score(point):
    return prod(sum(view(point, d)) for d in directions)


print("2:", max(score(point) for point in grid))
