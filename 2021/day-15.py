def input():
    with open("input-15.txt") as lines:
        for line in lines:
            yield line.strip()


grid = {}
for y, row in enumerate(input()):
    for x, risk in enumerate(row):
        grid[(x, y)] = int(risk)

start = (0, 0)
end = (x, y)


def neighbors(x, y):
    return {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}


def neighborhood(exploring, unexplored):
    done = set()
    candidate_paths = []

    for origin in exploring:
        destinations = neighbors(*origin) & unexplored
        if not destinations:  # this point is fully explored, don't search it again
            done.add(origin)
            continue
        for dest in destinations:
            candidate_paths.append((origin, dest))
    return done, candidate_paths


costs = {start: 0}
exploring = {start}
unexplored = set(grid.keys())


def cost(candidate_path):
    origin, dest = candidate_path
    return costs[origin] + grid[dest]


# while end not in costs:
#     stop_exploring, start_exploring = neighborhood(exploring, unexplored)
#     exploring -= stop_exploring
#     path = min(start_exploring, key=cost)
#     exploring.add(path[1])
#     unexplored.remove(path[1])
#     costs[path[1]] = cost(path)
# print("1:", costs[end])

# part2...holy shit, can I possibly use the same technique?
end = (499, 499)


def get(x, y):
    boost_x, x = divmod(x, 100)
    boost_y, y = divmod(y, 100)
    val = boost_x + boost_y + grid[(x, y)]
    return (val - 1) % 9 + 1


def cost(candidate_path):
    origin, dest = candidate_path
    return costs[origin] + get(*dest)


unexplored = set((x, y) for x in range(500) for y in range(500))  # cringe

i = 0
while end not in costs:
    stop_exploring, start_exploring = neighborhood(exploring, unexplored)
    exploring -= stop_exploring
    path = min(start_exploring, key=cost)
    exploring.add(path[1])
    unexplored.remove(path[1])
    costs[path[1]] = cost(path)

    i += 1
    if not i % 1000:
        print("--", i, "--")
print("2:", costs[end])
