with open("input/06.txt") as f:
    times = [int(i) for i in next(f).split()[1:]]
    bests = [int(i) for i in next(f).split()[1:]]

def distances(t):
    for i in range(t+1):
        yield (t - i) * i

prod = 1
for time, best in zip(times, bests):
    prod *= sum(1 for d in distances(time) if d > best)
print("1:", prod)

with open("input/06.txt") as f:
    time = int("".join(next(f).split()[1:]))
    best = int("".join(next(f).split()[1:]))
print("2:", sum(1 for d in distances(time) if d > best))