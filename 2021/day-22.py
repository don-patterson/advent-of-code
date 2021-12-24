from dataclasses import dataclass


@dataclass(frozen=True)
class Range:
    min: int
    max: int

    @property
    def length(self):
        return self.max - self.min + 1

    def intersection(self, other):
        if (start := max(self.min, other.min)) <= (end := min(self.max, other.max)):
            return Range(start, end)
        return None

    def subtract(self, other):
        if (intersection := self.intersection(other)) is None:
            yield self
            return

        if self.min < intersection.min:  # left side is non-empty
            yield Range(self.min, intersection.min - 1)
        if intersection.max < self.max:  # right side is non-empty
            yield Range(intersection.max + 1, self.max)

    def __repr__(self):
        return f"[{self.min}, {self.max}]"


@dataclass(frozen=True)
class Box:
    x: Range
    y: Range
    z: Range

    @property
    def volume(self):
        return self.x.length * self.y.length * self.z.length

    def intersection(self, other):
        return (
            (x := self.x.intersection(other.x))
            and (y := self.y.intersection(other.y))
            and (z := self.z.intersection(other.z))
            and Box(x, y, z)
        )

    def subtract(self, other):
        if (intersection := self.intersection(other)) is None:
            yield self
            return

        for x in self.x.subtract(intersection.x):
            # two big slices on the outsides
            yield Box(x, self.y, self.z)

        for y in self.y.subtract(intersection.y):
            # two columns between the slices
            yield Box(intersection.x, y, self.z)

        for z in self.z.subtract(intersection.z):
            # small columns above and below the x/y intersection
            yield Box(intersection.x, intersection.y, z)


def read_instruction(line):
    # line looks like: "on x=-10..39,y=-10..35,z=-19..32"
    on, ranges = line.split(" ")
    return on == "on", Box(*read_ranges(ranges))


def read_ranges(range_string):
    for d in range_string.split(","):
        _, values = d.split("=")
        start, end = values.split("..")
        yield Range(int(start), int(end))


with open("input-22.txt") as f:
    instructions = [read_instruction(line) for line in f]

nonoverlapping = set()
for on, cube in instructions:
    boxes = set()
    for box in nonoverlapping:
        boxes.update(box.subtract(cube))
    # now "boxes" is still non-overlapping, with a space carved out for the new cube
    if on:
        boxes.add(cube)
    nonoverlapping = boxes

init = Box(Range(-50, 50), Range(-50, 50), Range(-50, 50))
init_on = {b.intersection(init) for b in nonoverlapping}
print("1:", sum(b.volume for b in init_on if b is not None))
print("2:", sum(b.volume for b in nonoverlapping))
