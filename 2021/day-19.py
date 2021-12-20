from itertools import combinations, pairwise, permutations, takewhile
from functools import reduce
from collections import Counter


def all_rotations():
    """find all of the 24 rotations, based on where (1,2,3) ends up
    after a bunch of x, y, and z rotations
    """
    base_rotations = {
        "x": lambda p: (p[0], -p[2], p[1]),
        "y": lambda p: (p[2], p[1], -p[0]),
        "z": lambda p: (-p[1], p[0], p[2]),
    }

    start = (1, 2, 3)
    origin = {
        1: lambda p: p[0],
        -1: lambda p: -p[0],
        2: lambda p: p[1],
        -2: lambda p: -p[1],
        3: lambda p: p[2],
        -3: lambda p: -p[2],
    }

    def get_transform(end):
        """find a simplified function that moves `(1,2,3)` to `end`"""
        return lambda p: (origin[end[0]](p), origin[end[1]](p), origin[end[2]](p))

    observed = set()
    for x in range(4):
        for y in range(4):
            for z in range(4):
                rotations = (
                    [base_rotations["x"]] * x
                    + [base_rotations["y"]] * y
                    + [base_rotations["z"]] * z
                )
                result = reduce(lambda point, rot: rot(point), rotations, start)
                if result not in observed:
                    yield get_transform(result)
                    observed.add(result)


rotations = list(all_rotations())


def add(v1, v2):
    return tuple(a + b for a, b in zip(v1, v2))


class Scanner:
    def __init__(self, id, points=None, origin=(0, 0, 0)):
        self.id = id
        self.points = points or []
        self.origin = origin

    def coords(self, d):
        i = ["x", "y", "z"].index(d)
        return [p[i] for p in self.points]

    def count(self, d):
        return Counter(self.coords(d))

    def rotate(self, rotation):  # x, y, z
        return Scanner(self.id, [rotation(p) for p in self.points])

    def translate(self, q):
        return Scanner(self.id, [add(p, q) for p in self.points], origin=q)


scanners = []
with open("input-19.txt") as f:
    for line in f:
        s = Scanner(int(line.split()[2]))
        for value in takewhile(lambda v: v != "\n", f):
            s.points.append(tuple(int(i) for i in value.split(",")))
        scanners.append(s)


def intersects(count1, count2):
    """slide count2 from left to right until it aligns best with count1"""
    min1, max1 = min(count1.keys()), max(count1.keys())
    min2, max2 = min(count2.keys()), max(count2.keys())
    for offset in range(min1 - max2, max1 - min2 + 1):
        off_count2 = {coord + offset: count for coord, count in count2.items()}
        intersection = Counter(
            {
                k: min(count1[k], off_count2[k])
                for k in count1.keys() & off_count2.keys()
            }
        )
        if intersection.total() >= 12:
            return offset
    return None


def find_aligned(s0, s1):
    x = s0.count("x")
    y = s0.count("y")
    z = s0.count("z")
    for r in rotations:
        s = s1.rotate(r)
        ox = intersects(x, s.count("x"))
        if ox is None:
            continue
        oy = intersects(y, s.count("y"))
        if oy is None:
            continue
        oz = intersects(z, s.count("z"))
        if oz is None:
            continue
        # confirm
        s = s.translate((ox, oy, oz))
        if len(set(s0.points) & set(s.points)) < 12:
            continue
        return s
    return None


aligned = [scanners[0]]
remaining = scanners[1:]


def whatsleft():
    for a in reversed(aligned):
        for r in remaining:
            yield a, r


while remaining:
    print(len(remaining), "remain")
    for a, r in whatsleft():
        new_r = find_aligned(a, r)
        if new_r:
            remaining.remove(r)
            aligned.append(new_r)


def dist(p, q):
    return sum(abs(a - b) for a, b in zip(p, q))


print("1:", len(set.union(*[set(a.points) for a in aligned])))
print("2:", max(dist(s0.origin, s1.origin) for s0, s1 in combinations(aligned, 2)))
