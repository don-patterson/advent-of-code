with open("input/06.txt") as f:
    input = f.read()


def find(size):
    for end in range(size, len(input)):
        if len(set(input[end - size : end])) == size:
            return end


print("1:", find(4))
print("2:", find(14))
