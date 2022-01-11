from collections import defaultdict
from dataclasses import dataclass
from itertools import product


@dataclass
class Box:
    lower: tuple
    upper: tuple

    @property
    def points(self):
        return product(
            range(self.lower[0], self.upper[0] + 1),
            range(self.lower[1], self.upper[1] + 1),
        )


instructions = []
with open("input/06.txt") as f:
    for line in f:
        *operation, lower, _through, upper = line.split(" ")
        x1, y1 = lower.split(",")
        x2, y2 = upper.split(",")
        x1, x2 = sorted([int(x1), int(x2)])
        y1, y2 = sorted([int(y1), int(y2)])
        assert x1 <= x2
        assert y1 <= y2
        instructions.append((operation[-1], Box(lower=(x1, y1), upper=(x2, y2))))


# naive way: keep a big list
lights = defaultdict(bool)


operations = {
    "off": lambda _: False,
    "on": lambda _: True,
    "toggle": lambda light: not light,
}


for operator, box in instructions:
    func = operations[operator]
    for point in box.points:
        lights[point] = func(lights[point])

print("1:", sum(lights.values()))


# part 2: you should probably just get the area of the square
# but ... since I have all this machinery
lights = defaultdict(int)
operations = {
    "off": lambda light: max(light - 1, 0),
    "on": lambda light: light + 1,
    "toggle": lambda light: light + 2,
}

for operator, box in instructions:
    func = operations[operator]
    for point in box.points:
        lights[point] = func(lights[point])

print("2:", sum(lights.values()))
