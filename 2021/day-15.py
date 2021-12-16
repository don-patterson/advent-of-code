from bisect import insort


with open("input-15.txt") as f:
    input = f.read().splitlines()


risk = {(x, y): int(v) for y, row in enumerate(input) for x, v in enumerate(row)}
start = (0, 0)
end = (99, 99)


def neighbors(point, max=99):
    x, y = point
    if x < max:
        yield x + 1, y
    if x > 0:
        yield x - 1, y
    if y < max:
        yield x, y + 1
    if y > 0:
        yield x, y - 1


path_risk = {point: 999999 for point in risk}
exploring = [(start, 0)]


def update_path_risk(point, current_risk):
    if (new_risk := current_risk + risk[point]) < path_risk[point]:
        path_risk[point] = new_risk
        insort(exploring, (point, new_risk), key=lambda v: -v[1])


def explore(point, current_risk):
    for neighbor in neighbors(point):
        update_path_risk(neighbor, current_risk)


point = None
while point != end:
    point, current_risk = exploring.pop()
    explore(point, current_risk)

print("1:", path_risk[end])


# part 2 copy pasta...could have made this a little cleaner/reusable
# but at least now it runs fast
end = (499, 499)


def risk2(point):
    x, y = point
    boost_x, x = divmod(x, 100)
    boost_y, y = divmod(y, 100)
    val = boost_x + boost_y + risk[(x, y)]
    return (val - 1) % 9 + 1


path_risk = {(x, y): 999999 for x in range(500) for y in range(500)}
exploring = [(start, 0)]


def update_path_risk(point, current_risk):
    if (new_risk := current_risk + risk2(point)) < path_risk[point]:
        path_risk[point] = new_risk
        insort(exploring, (point, new_risk), key=lambda v: -v[1])


def explore(point, current_risk):
    for neighbor in neighbors(point, max=499):
        update_path_risk(neighbor, current_risk)


point = None
while point != end:
    point, current_risk = exploring.pop()
    explore(point, current_risk)

print("2:", path_risk[end])
