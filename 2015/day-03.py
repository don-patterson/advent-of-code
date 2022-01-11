with open("input/03.txt") as f:
    input = f.read()

moves = {
    "<": lambda x, y: (x - 1, y),
    ">": lambda x, y: (x + 1, y),
    "^": lambda x, y: (x, y + 1),
    "v": lambda x, y: (x, y - 1),
}

location = (0, 0)
visited = {location}
for direction in input:
    location = moves[direction](*location)
    visited.add(location)

print("1:", len(visited))


locations = [(0, 0), (0, 0)]
visited = set(locations)
for i, direction in enumerate(input):
    locations[i % 2] = moves[direction](*locations[i % 2])
    visited.add(locations[i % 2])

print("2:", len(visited))
