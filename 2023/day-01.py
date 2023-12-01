with open("input/01.txt") as f:
    input = f.read().splitlines()


def digits(line):
    for c in line:
        if c.isdigit():
            yield int(c)

def val(line):
    d = list(digits(line))
    return 10*d[0] + d[-1]

replacements = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def digits2(line):
    for i, c in enumerate(line):
        if c.isdigit():
            yield int(c)
            continue
        for n, pattern in enumerate(replacements, start=1):
            if line[i:].startswith(pattern):
                yield n
                break

def val2(line):
    d = list(digits2(line))
    return 10*d[0] + d[-1]

print("1:", sum(val(line) for line in input))
print("2:", sum(val2(line) for line in input))
