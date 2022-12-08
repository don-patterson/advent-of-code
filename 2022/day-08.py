from math import prod

height = {}
with open("input/08.txt") as f:
    for y, row in enumerate(f):
        for x, h in enumerate(row.strip()):
            height[(x, y)] = int(h)
x_range = range(x + 1)
y_range = range(y + 1)

directions = ((-1, 0), (1, 0), (0, 1), (0, -1))


def ray(start, direction):
    x, y = start
    step_x, step_y = direction
    while (x := x + step_x) in x_range and (y := y + step_y) in y_range:
        yield x, y


known_visible = set()


def is_visible(start):
    visible = start in known_visible or any(
        all(height[p] < height[start] for p in ray(start, d)) for d in directions
    )
    if visible:
        known_visible.add(start)
    return visible


for y in y_range:
    for x in x_range:
        if is_visible((x, y)):
            print(f"\033[96m{height[(x,y)]}\033[0m", end="")
        else:
            print(height[(x, y)], end="")
    print()

print("1:", len(known_visible))


def view(start, direction):
    for p in ray(start, direction):
        yield 1
        if height[p] >= height[start]:
            break


def score(point):
    return prod(sum(view(point, d)) for d in directions)


print("2:", max(score(point) for point in height))
