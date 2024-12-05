from os.path import dirname

grid = {}
with open(dirname(__file__) + "/input/04.txt") as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line):
            grid[(x,y)] = c

vec = [(x,y) for x in [-1,0,1] for y in [-1,0,1]]
vec.remove((0,0))

def word(p, v):
    w = ""
    for i in [0, 1,2,3]:
        w += grid.get((p[0] + i*v[0], p[1] + i*v[1]), "_")
    return "".join(w)

print("1:", sum(1 for p in grid for v in vec if word(p,v) == "XMAS"))

def corners(p):
    return [
        grid.get((p[0]-1, p[1]-1), "_") + grid.get((p[0]+1, p[1]+1), "_"),
        grid.get((p[0]-1, p[1]+1), "_") + grid.get((p[0]+1, p[1]-1), "_")
    ]

print("2:", sum(1 for p in grid if grid[p] == "A" and all(c in ["MS", "SM"] for c in corners(p))))
