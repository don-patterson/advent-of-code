from string import ascii_lowercase

grid = {}
with open("input/12.txt") as f:
    for y, row in enumerate(f):
        for x, c in enumerate(row.strip()):
            if c == "S":
                c = "a"
                start = x, y
            if c == "E":
                c = "z"
                end = x, y
            grid[(x, y)] = ascii_lowercase.index(c)


def neighbors(point):
    x, y = point
    for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if p in grid and grid[p] - grid[point] <= 1:
            yield p


def neighbors2(point):
    x, y = point
    for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if p in grid and grid[point] - grid[p] <= 1:
            yield p


distance = {p: 9999 for p in grid}
distance[start] = 0
visited = set()

while end not in visited:
    current = min(distance.keys() - visited, key=lambda k: distance[k])
    for neighbor in neighbors(current):
        if distance[current] + 1 < distance[neighbor]:
            distance[neighbor] = distance[current] + 1
    visited.add(current)

print("1:", distance[end])


distance = {p: 9999 for p in grid}
distance[end] = 0
visited = set()

while len(visited) != len(grid):
    current = min(distance.keys() - visited, key=lambda k: distance[k])
    for neighbor in neighbors2(current):
        if distance[current] + 1 < distance[neighbor]:
            distance[neighbor] = distance[current] + 1
    visited.add(current)

print("2:", min(distance[p] for p in grid if grid[p] == ascii_lowercase.index("a")))
