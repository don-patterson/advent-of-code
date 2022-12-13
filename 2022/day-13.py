from functools import cmp_to_key

pairs = []
with open("input/13.txt") as f:
    for pair in f.read().strip().split("\n\n"):
        left, right = pair.split("\n")
        pairs.append([eval(left), eval(right)])


def cmp(left, right):
    def _list_cmp(L, R):
        for i, j in zip(L, R):
            if (c := cmp(i, j)) != 0:
                return c
        return len(L) - len(R)

    return {
        (int, int): lambda i, j: i - j,
        (int, list): lambda i, L: cmp([i], L),
        (list, int): lambda L, j: cmp(L, [j]),
        (list, list): _list_cmp,
    }[type(left), type(right)](left, right)


print("1:", sum(i + 1 for i, pair in enumerate(pairs) if cmp(*pair) < 0))

flat = [p for pair in pairs for p in pair] + [[], [[2]], [[6]]]
flat.sort(key=cmp_to_key(cmp))
print("2:", flat.index([[2]]) * flat.index([[6]]))
