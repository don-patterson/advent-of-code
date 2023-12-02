from math import prod

empty = {"red": 0, "green": 0, "blue": 0}
games = {}
with open("input/02.txt") as f:
    for line in f:
        game, rest = line.strip().split(": ")
        game = game.split()[1]
        games[game] = []
        for draw in rest.split("; "):
            counts = {**empty}
            for val in draw.split(", "):
                n, color = val.split()
                counts[color] += int(n)
            games[game].append(counts)

bag = {"red": 12, "green": 13, "blue": 14}

total_valid = 0
for id, draws in games.items():
    if all(draw[k] <= bag[k] for k in bag for draw in draws):
        total_valid += int(id)
print("1:", total_valid)

power = 0
for id, draws in games.items():
    smallest = {**empty}
    for draw in draws:
        for k in bag:
            smallest[k] = max(smallest[k], draw[k])
    power += prod(smallest.values())
print("2:", power)