def input():
    with open("input-12.txt") as lines:
        for line in lines:
            yield line.strip()


edges = {tuple(line.split("-")) for line in input()}
edges |= {(b, a) for a, b in edges}

if any(a.isupper() and b.isupper() for a, b in edges):
    raise Exception("uh oh, infinite loops!")


def not_in(path, node):
    return node not in path


def one_duplicate(path, node):
    lower = [n for n in path if n.islower()]
    return node not in lower or len(lower) == len(set(lower))


def extensions(*path, check=None):
    if path[-1] == "end":
        yield path
        return

    for (a, b) in edges:
        if b == "start":
            continue

        if a == path[-1] and (b.isupper() or check(path, b)):
            yield from extensions(*path, b, check=check)


print("1:", sum(1 for _ in extensions("start", check=not_in)))
print("2:", sum(1 for _ in extensions("start", check=one_duplicate)))
