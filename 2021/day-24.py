from itertools import pairwise, product, islice
import sys


class ALU:
    def __init__(self, instructions):
        self.inputs = None
        self.instructions = instructions
        self.reset()

    def reset(self, state=(0, 0, 0, 0)):
        (self.w, self.x, self.y, self.z) = state

    @property
    def state(self):
        return (self.w, self.x, self.y, self.z)

    def _int_or_attr(self, a):
        try:
            return int(a)
        except ValueError:
            return getattr(self, a)

    def __call__(self, *inputs, state=None):
        if state:
            self.reset(state)
        self.inputs = iter(inputs)
        for instruction in self.instructions:
            func, var, *args = instruction.split()
            arg = args[0] if args else 0
            self.operate(func, var, self._int_or_attr(arg))
            # print(f"{instruction} -> {self.state}")
        # print()
        return (self.w, self.x, self.y, self.z)

    def operate(self, func, var, value):
        op = getattr(self, f"_{func}")
        setattr(self, var, op(getattr(self, var), value))

    def _inp(self, *_):
        return next(self.inputs)

    def _add(self, a, b):
        return a + b

    def _mul(self, a, b):
        return a * b

    def _mod(self, a, b):
        return a % b

    def _div(self, a, b):
        if a < 0:
            if b < 0:
                return a // b
            return -((-a) // b)
        if b < 0:
            return -(a // (-b))
        return a // b

    def _eql(self, a, b):
        return 1 if a == b else 0


with open("input-24.txt") as f:
    validator = ALU([line.strip() for line in f])


def split(n):
    for digit in str(n):
        yield int(digit)


print(validator(*split(99996919281931)))

# thought I found 99996919281931 to work by calculating them by hand...must have missed somewhere

sys.exit()
# the following didn't work!

# lol
# def split(n):
#     for digit in str(n):
#         yield int(digit)


# for i in range(99999999999999, 10000000000000, -1):
#     if validator(*split(i))[-1] == 0:
#         print("found it!", i)
#         break


# try to reverse engineer each block. they seem to be independent. just looking at them
# they all start with input w, and setting x = z
blocks = []
with open("input-24.txt") as f:
    for instruction in f:
        if instruction.startswith("inp"):
            blocks.append([])
        blocks[-1].append(instruction.strip())
programs = [ALU(block) for block in blocks]


def check_x_and_y(program):
    # we know w is given in input, and z seems to be carried through
    # but do x and y matter?
    for w, x, y in product(range(1, 10), repeat=3):
        for z in [-1234, -45, -1, 0, 1, 10, 67, 1993]:
            arbitrary = program(w, state=(0, 1, 7, z))
            if program(w, state=(0, x, y, z))[-1] != arbitrary[-1]:
                print("difference!")


# for program in programs:
#     check_x_and_y(program)
# # no differences!  so each block is just a function of w (input) and z


def z_plus():
    i = 0
    while True:
        yield i
        i += 1


def find_z_values(program, target):
    # see if certain z values evaluate to target. let's try positive z first...
    for w in range(1, 10):
        for z in z_plus():
            if program(w, state=(0, 0, 0, z))[-1] == target(w):
                yield (w, z)
                break


def take(iterable, n):
    return list(islice(iterable, n))


def line(p1, p2):
    w1, z1 = p1
    w2, z2 = p2
    assert w2 == w1 + 1
    slope = z2 - z1
    intercept = z1 - slope * w1
    return slope, intercept


def prove_linear(program, target):
    results = take(find_z_values(program, target), 9)
    lines = set(line(p1, p2) for p1, p2 in pairwise(results))
    assert len(lines) == 1
    slope, intercept = lines.pop()
    print(f"0 when z={intercept}{slope:+}w")
    return lambda w: intercept + slope * w


# not sure if any of that works. now after doing a few manually, I see
# that they all have a net addition to z, like z += w + 16, or z += w + 3.
# maybe that's true in general?


def get_outputs(program, z_range):
    for w, z in product(range(1, 10), z_range):
        yield program(w, state=(0, 0, 0, z))[-1]


z_values = []
for i, program in enumerate(programs):
    if i == 0:
        z_values.append(set(get_outputs(programs[i], z_range=[0])))
    else:
        z_values.append(set(get_outputs(programs[i], z_range=z_values[i - 1])))
    print(i, sorted(z_values[i])[:10], len(z_values[i]))
