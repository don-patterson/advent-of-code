from aoc import lines

closing = {
    ")": {"score": 3, "closes": "("},
    "]": {"score": 57, "closes": "["},
    "}": {"score": 1197, "closes": "{"},
    ">": {"score": 25137, "closes": "<"},
}


def error_score(instruction):  # return score, [still_open...]
    stack = []
    for c in instruction:
        if c in closing:
            if stack[-1] == closing[c]["closes"]:
                stack.pop()
            else:
                return closing[c]["score"], []
        else:
            stack.append(c)
    return 0, stack


print("1:", sum(error_score(line)[0] for line in lines("input-10.txt")))


def close_score(stack):
    total = 0
    for c in reversed(stack):
        total = 5 * total + "_([{<".index(c)
    return total


closing_scores = []

for line in lines("input-10.txt"):
    e, stack = error_score(line)
    if e > 0:
        continue
    closing_scores.append(close_score(stack))

print("2:", sorted(closing_scores)[(len(closing_scores) - 1) // 2])
