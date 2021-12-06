from collections import Counter
from aoc import lines


def int_range(a, b):
    if a <= b:
        return range(a, b + 1)
    return range(a, b - 1, -1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x_range(self, other):
        return int_range(self.x, other.x)

    def y_range(self, other):
        return int_range(self.y, other.y)

    def flat_coordinates(self, other):
        if self.x == other.x:
            yield from ((self.x, y) for y in self.y_range(other))

        if self.y == other.y:
            yield from ((x, self.y) for x in self.x_range(other))

    def diagonal_coordinates(self, other):
        if self.x == other.x or self.y == other.y:
            return
        yield from zip(self.x_range(other), self.y_range(other))


flats = Counter()
diagonals = Counter()
for p1, _, p2 in lines("input-05.txt", shape=[str, str, str]):
    start = Point(*[int(i) for i in p1.split(",")])
    end = Point(*[int(i) for i in p2.split(",")])
    for point in start.flat_coordinates(end):
        flats[point] += 1
    for point in start.diagonal_coordinates(end):
        diagonals[point] += 1

diagonals += flats

print("1:", sum(1 for c in flats.values() if c > 1))
print("1:", sum(1 for c in diagonals.values() if c > 1))
