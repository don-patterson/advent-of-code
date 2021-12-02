from aoc import lines

# part 1
input = lines("input-01.txt", shape=int)
a = next(input)
increase_count = 0

for b in input:
    if a < b:
        increase_count += 1
    a = b

print("1:", increase_count)


# part 2
input = lines("input-01.txt", shape=int)
a, b, c = next(input), next(input), next(input)
increase_count = 0

for d in input:
    if a < d:
        increase_count += 1
    a, b, c = b, c, d

print("2:", increase_count)
