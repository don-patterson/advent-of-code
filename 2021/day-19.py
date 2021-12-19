from itertools import combinations, pairwise, takewhile


projections = {
    "+x": lambda p: p[0],
    "-x": lambda p: -p[0],
    "+y": lambda p: p[1],
    "-y": lambda p: -p[1],
    "+z": lambda p: p[2],
    "-z": lambda p: -p[2],
}


def offsets(values):
    m = min(values)
    return set(v - m for v in values)


class Scanner:
    def __init__(self, id):
        self.id = id
        self.points = []

    @property
    def first(self):
        return self.points[0]

    @property
    def last(self):
        return self.points[-1]

    def project(self, d):
        proj = projections[d]
        for p in self.points:
            yield proj(p)

    def offsets(self, d):
        return offsets(list(self.project(d)))

    def __repr__(self) -> str:
        return f"S({self.id})"
        # return f"S[{self.id}:{self.first}...{self.last}]"


def max_overlap(offsets1, offsets2):
    """slide offsets2 to the right until it maximally overlaps with offsets1
    i.e. offsets1 = {0, 2, 7, 12, 15}
     and offsets2 = {0, 5, 8}

    try:
     0:          offsets1 = {0, 2, 7, 12, 15}
       intersect offsets2 = {0, 5, 8}

     1:          offsets1 =     {0, 2, 7, 12, 15}
       intersect offsets2 + 1 = {1, 6, 9}
     ...
     7:          offsets1 =     {0, 2, 7, 12, 15}
       intersect offsets2 + 7 = {7, 12, 15}
              for maximal intersection of 3
     ...
     15: would be the last attempt
    """
    best = (0, 0)  # (size, slide)
    for slide in range(max(offsets1) + 1):
        adjusted_offsets2 = {e + slide for e in offsets2}
        size = len(offsets1 & adjusted_offsets2)
        if size > best[0]:
            best = (size, slide)
    return best


def find_overlap(s0, s1):
    for d0 in ["+x", "+y", "+z"]:
        off0 = s0.offsets(d0)
        for d1 in projections:
            size, slide = max_overlap(off0, s1.offsets(d1))
            if size >= 12:
                print(s0.id, s1.id, "overlaps", d0, d1, size, slide)


scanners = []
with open("input-19.txt") as f:
    for line in f:
        s = Scanner(int(line.split()[2]))
        for value in takewhile(lambda v: v != "\n", f):
            s.points.append(tuple(int(i) for i in value.split(",")))
        scanners.append(s)


for s0, s1 in combinations(scanners, 2):
    find_overlap(s0, s1)
