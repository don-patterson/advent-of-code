elves = [[]]
with open("input/01.txt") as f:
    for line in f:
        if line == "\n":
            elves.append([])
        else:
            elves[-1].append(int(line))

counts = sorted(sum(elf) for elf in elves)
print("1", counts[-1])
print("2", sum(counts[-3:]))
