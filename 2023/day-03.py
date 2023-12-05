from math import floor, log10
from collections import namedtuple



symbols = {}
ids = {}
vals = {}

cur_id = 0
cur_val = 0

with open("input/03.txt") as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line):
            if c.isdigit():
                cur_val = 10*cur_val + int(c)
                ids[(x, y)] = cur_id
                continue

            if cur_val > 0:
                vals[cur_id] = cur_val
                cur_id += 1
                cur_val = 0

            if c == "." or c == "\n":
                continue

            symbols[(x, y)] = c

def near(x, y):
    for ny in [y-1, y, y+1]:
        for nx in [x-1, x, x+1]:
            n_id = ids.get((nx, ny))
            if n_id is not None:
                yield n_id

part_ids = set()
gear_total = 0
for x, y in symbols:
    neighbors = set(near(x, y))
    part_ids.update(neighbors)
    if len(neighbors) == 2:
        id_a, id_b = neighbors
        gear_total += vals[id_a] * vals[id_b]

print("1:", sum(vals[i] for i in part_ids))
print("2:", gear_total)