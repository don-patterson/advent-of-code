from copy import deepcopy

with open("input/05.txt") as f:
    crates, moves = f.read().rstrip().split("\n\n")
    moves = moves.split("\n")

    *crates, labels = crates.split("\n")
    labels = labels.split()

stacks = {label: [] for label in labels}
for row in reversed(crates):
    for label in labels:
        crate = row[4 * int(label) - 3]
        if crate != " ":
            stacks[label].append(crate)

stacks2 = deepcopy(stacks)


def move9000(count, fr, to):
    for _ in range(int(count)):
        stacks[to].append(stacks[fr].pop())


def move9001(count, fr, to):  # too lazy to optimize...
    tempstack = []
    for _ in range(int(count)):
        tempstack.append(stacks2[fr].pop())
    for _ in range(int(count)):
        stacks2[to].append(tempstack.pop())


for line in moves:
    _, count, _, fr, _, to = line.split()
    move9000(count, fr, to)
    move9001(count, fr, to)
print("1:", "".join(stacks[label][-1] for label in labels))
print("2:", "".join(stacks2[label][-1] for label in labels))
