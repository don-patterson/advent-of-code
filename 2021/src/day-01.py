def input():
    with open("input-01.txt") as text:
        for line in text:
            yield int(line)


# part 1
numbers = input()
a = next(numbers)
increase_count = 0

for b in numbers:
    if a < b:
        increase_count += 1
    a = b

print("1:", increase_count)


# part 2
numbers = input()
a, b, c = next(numbers), next(numbers), next(numbers)
increase_count = 0

for d in numbers:
    if a < d:
        increase_count += 1
    a, b, c = b, c, d

print("2:", increase_count)
