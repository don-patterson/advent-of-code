class Range:
    def __init__(self, start, length):
        self.start = start
        assert length > 0
        self.length = length
    
    @property
    def end(self):
        return self.start + self.length - 1

    def __contains__(self, n):
        return 0 <= (n - self.start) < self.length

    def __add__(self, n):
        return Range(self.start+n, self.length)

    def intersect(self, other):
        if self.start > other.end or self.end < other.start:
            return None
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        return Range(start=start, length=end-start+1)

    def __repr__(self):
        return f"Range({self.start},{self.length})"

class Mapping:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __call__(self, n):
        if isinstance(n, Range):
            intersection = self.src.intersect(n)
            return intersection and (intersection + (self.dest.start - self.src.start))
        else:
            return self.dest.start - self.src.start + n


mappings = {}

with open("input/05.txt") as f:
    seeds = [int(s) for s in next(f).split()[1:]]
    assert next(f) == "\n"
    
    for line in f:
        if line.endswith(":\n"):
            src, dest = line.split()[0].split("-to-")
            mappings[(src, dest)] = []
            continue
        if line == "\n":
            continue

        d, s, l = [int(i) for i in line.split()]
        mappings[(src, dest)].append(Mapping(src=Range(start=s, length=l),
                                             dest=Range(start=d, length=l)))


def get_dest(src_type):
    dests = [dest for src,dest in mappings if src == src_type]
    if len(dests) != 1:
        print("uh oh")
    return dests[0]

def get_mapped(src, val):
    dest = get_dest(src)
    for mapping in mappings[(src, dest)]:
        if val in mapping.src:
            return dest, mapping(val)
    return dest, val

def get_location(src, val):
    while src != "location":
        src, val = get_mapped(src, val)
    return val


locations = [get_location("seed", val) for val in seeds]
print("1:", min(locations))


ranges = []
range_type = "seed"
pairs = iter(seeds)
for start in pairs:
    length = next(pairs)
    ranges.append(Range(start, length))

def map_all(ranges, range_type):
    dest_type = get_dest(range_type)
    mapped = []
    for mapping in mappings[(range_type, dest_type)]:
        for r in ranges:
            mapped.append(mapping(r))
    return [m for m in mapped if m is not None], dest_type

while range_type != "location":
    ranges, range_type = map_all(ranges, range_type)

print("2:", min(r.start for r in ranges))