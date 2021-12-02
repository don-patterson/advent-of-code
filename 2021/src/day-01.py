from aoc_common import load_ints

input = load_ints("input-01.txt")

# part 1
[prev, *remaining] = input
increase_count = 0

for value in remaining:
    if prev < value:
        increase_count += 1
    prev = value

print("1:", increase_count)


# part 2
group_count = len(input) - 2
groups = [input[i : i + 3] for i in range(group_count)]

[prev, *remaining] = [sum(group) for group in groups]
increase_count = 0

for value in remaining:
    if prev < value:
        increase_count += 1
    prev = value

print("2:", increase_count)
