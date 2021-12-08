from aoc import lines

entries = []
for line in lines("input-08.txt"):
    [*digits, _, a, b, c, d] = line.split()
    entries.append({"in": digits, "out": [a, b, c, d]})

unique = {2, 3, 4, 7}

print(
    "1:",
    sum(sum(1 for o in entry["out"] if len(o) in unique) for entry in entries),
)


# part 2....
def find_by_length(length, entry):
    for segment in entry["in"]:
        if len(segment) == length:
            yield set(segment)


def unscramble(entry):
    [_1] = find_by_length(2, entry)
    [_4] = find_by_length(4, entry)
    [_7] = find_by_length(3, entry)
    [_8] = find_by_length(7, entry)

    # of 2, 3, 5, the only one that intersects fully with 1 is 3
    _3 = None
    for seg in find_by_length(5, entry):
        if len(_1 - seg) == 0:
            if _3 is not None:
                raise Exception("found two 3s!")
            _3 = seg

    # 2 intersects with 4 in two places, 5 intersects with 4 in 3 places
    [_2, _5] = list(seg for seg in find_by_length(5, entry) if seg != _3)
    if len(_4 - _2) != 2:  # then we got it backwards
        _2, _5 = _5, _2

    # what's left? 0, 6, 9
    # 6 is the only one that doesn't intersect fully with 1
    _6 = None
    for seg in find_by_length(6, entry):
        if len(_1 - seg) != 0:
            if _6 is not None:
                raise Exception("found two 6s!")
            _6 = seg

    # 9 intersects fully with 4
    [_0, _9] = list(seg for seg in find_by_length(6, entry) if seg != _6)
    if len(_4 - _9) != 0:  # then we got it backwards
        _0, _9 = _9, _0

    # not my proudest moment:
    return {
        "".join(sorted(_0)): "0",
        "".join(sorted(_1)): "1",
        "".join(sorted(_2)): "2",
        "".join(sorted(_3)): "3",
        "".join(sorted(_4)): "4",
        "".join(sorted(_5)): "5",
        "".join(sorted(_6)): "6",
        "".join(sorted(_7)): "7",
        "".join(sorted(_8)): "8",
        "".join(sorted(_9)): "9",
    }


outputs = []
for entry in entries:
    digit_map = unscramble(entry)
    digits = [digit_map["".join(sorted(o))] for o in entry["out"]]
    outputs.append(int("".join(digits)))


print("2:", sum(outputs))
