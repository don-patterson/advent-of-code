def input():
    with open("input-13.txt") as lines:
        for line in lines:
            yield line.strip()


lines = input()
points = set()
folds = []

for line in lines:
    if not line:
        break
    x, y = line.split(",")
    points.add((int(x), int(y)))

for line in lines:
    direction, value = line.split("=")
    folds.append({direction[-1]: int(value)})


def fold1d(point, along):
    if along is None or point < along:
        return point

    if point == along:
        raise Exception("this wasn't supposed to happen!")

    return 2 * along - point


def fold(a, b, x=None, y=None):
    return fold1d(a, x), fold1d(b, y)


folded = {fold(a, b, **folds[0]) for a, b in points}
print("1:", len(folded))


def graph(points):
    max_x = max(a for a, _ in points)
    max_y = max(b for _, b in points)

    for b in range(max_y + 1):
        for a in range(max_x + 1):
            print("#" if (a, b) in points else ".", end="")
        print()


for f in folds:
    points = {fold(a, b, **f) for a, b in points}

print("2:")
graph(points)
