from functools import partial


maxsize = 2 ** 16 - 1
NOT = lambda w: maxsize - w
AND = lambda w1, w2: w1 & w2
OR = lambda w1, w2: w1 | w2
LSHIFT = lambda amount, w: (w << amount) & maxsize
RSHIFT = lambda amount, w: w >> amount
ID = lambda w: w

resolved = {}  # wire: value
unresolved = {}  # output_wire: ({input_wires}, func)


def read(line):
    inputs, output = line.split(" -> ")
    match inputs.split():
        case ["NOT", w]:
            func, *args = NOT, w
        case [w, "LSHIFT", amount]:
            func, *args = LSHIFT, amount, w
        case [w, "RSHIFT", amount]:
            func, *args = RSHIFT, amount, w
        case [w1, "AND", w2]:
            func, *args = AND, w1, w2
        case [w1, "OR", w2]:
            func, *args = OR, w1, w2
        case [w]:
            func, *args = ID, w
        case _:
            print(line)
            raise Exception("missed")

    while args and args[0].isdigit():
        func = partial(func, int(args[0]))
        args = args[:1]

    if args:
        unresolved[output] = args, func
    else:
        resolved[output] = func()


with open("input/07.txt") as f:
    for line in f:
        read(line)

print(unresolved)
