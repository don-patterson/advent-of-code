with open("input/10.txt") as f:
    input = [line.split() for line in f]

ops = iter(input)

signal = 0
x = 1
addx = None
for cycle in range(1, 241):
    if cycle % 40 == 20:
        signal += cycle * x

    pixel = (cycle - 1) % 40
    if pixel in (x - 1, x, x + 1):
        print("#", end="")
    else:
        print(".", end="")
    if pixel == 39:
        print()

    if addx is None:
        # get a new operation
        match next(ops):
            case ["addx", amount]:
                addx = int(amount)
        continue
    else:
        # finish the addition
        x += addx
        addx = None

print("1:", signal)
print("2:", "^^")
