SAND_SOURCE = (500, 0)


def parse(point_str):
    return [int(i) for i in point_str.split(",")]


def points(x1, y1, x2, y2):
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            yield x, y


grid = set()
with open("input/14.txt") as f:
    for line in f:
        point_from, *remaining = [parse(p) for p in line.split(" -> ")]
        for point_to in remaining:
            grid.update(points(*point_from, *point_to))
            point_from = point_to

ymax = max(y for _, y in grid) + 1


def below(x, y):
    if y == ymax:
        return None  # resting

    for p in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)):
        if p not in grid:
            return p

    return None  # resting


def add_sand():
    sand = SAND_SOURCE
    while p := below(*sand):
        sand = p
    return sand


count = 0
while resting_point := add_sand():
    if resting_point[1] == ymax:
        break
    count += 1
    grid.add(resting_point)
print("1:", count)

while resting_point := add_sand():
    count += 1
    grid.add(resting_point)
    if resting_point == SAND_SOURCE:
        break
print("2:", count)
