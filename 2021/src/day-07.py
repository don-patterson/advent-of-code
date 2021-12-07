from aoc import lines

positions = []
for line in lines("input-07.txt"):
    positions.extend(int(i) for i in line.split(","))

start, end = min(positions), max(positions)


def cost(a, b):
    d = abs(a - b)
    return d * (d + 1) // 2


print("1:", min(sum(abs(p - i) for i in positions) for p in range(start, end)))
print("2:", min(sum(cost(p, i) for i in positions) for p in range(start, end)))
