from os.path import dirname
lines = []
with open(dirname(__file__) + "/input/02.txt") as f:
    for line in f:
        lines.append([int(i) for i in line.split()])

def safe(line):
    return all((b-a) in {1,2,3} for a,b in zip(line, line[1:]))

print("1:", sum(1 for line in lines if (safe(line) or safe(line[::-1]))))

def drops(line):
    for i in range(len(line)):
        yield line[:i] + line[i+1:]

def anysafe(line):
    return safe(line) or safe(line[::-1]) or any(
        safe(l) or safe(l[::-1])
        for l in drops(line)
    )

print("2:", sum(1 for line in lines if anysafe(line)))
