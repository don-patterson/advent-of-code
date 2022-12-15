from re import findall


class Sensor:
    def __init__(self, x, y, radius) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def covers(self, x, y):
        return abs(self.x - x) + abs(self.y - y) <= self.radius

    def x_coverage_at(self, y):
        overlap = self.radius - abs(y - self.y)
        return range(self.x - overlap, self.x + overlap + 1)

    def perimeter(self):
        # all points r=(radius+1) from x,y
        r = self.radius + 1
        left = self.x - r, self.y
        right = self.x + r, self.y
        top = self.x, self.y + r
        bottom = self.x, self.y - r

        x, y = left
        while (x, y) != top:
            yield x, y
            x += 1
            y += 1

        while (x, y) != right:
            yield x, y
            x += 1
            y -= 1

        while (x, y) != bottom:
            yield x, y
            x -= 1
            y -= 1

        while (x, y) != left:
            yield x, y
            x -= 1
            y += 1


sensors = []
beacons = set()
with open("input/15.txt") as f:
    for line in f:
        x1, y1, x2, y2 = [int(i) for i in findall("-?\d+", line)]
        sensors.append(Sensor(x1, y1, radius=abs(x1 - x2) + abs(y1 - y2)))
        beacons.add((x2, y2))

covered = set(x for s in sensors for x in s.x_coverage_at(y=2_000_000))
for x, y in beacons:
    if y == 2_000_000:
        covered.remove(x)

print("1:", len(covered))


# find the only uncovered spot between (0,0) and (4M, 4M), I think?
# it is going to be on the perimeter of a beacon

for sensor in sensors:
    for x, y in sensor.perimeter():
        if (
            0 <= x <= 4_000_000
            and 0 <= y <= 4_000_000
            and all(not s.covers(x, y) for s in sensors)
        ):
            print("found one!:", x, y, 4_000_000 * x + y)
