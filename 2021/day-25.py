with open("input-25.txt") as f:
    rows = [list(line.strip()) for line in f]

# # example:
# rows = [
#     list(row)
#     for row in """\
# v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>
# """.split()
# ]

width = len(rows[0])
height = len(rows)


def display():
    print("\n".join("".join(row) for row in rows) + "\n")


def can_move_right(i, j):
    return rows[j][i] == ">" and rows[j][(i + 1) % width] == "."


def can_move_down(i, j):
    return rows[j][i] == "v" and rows[(j + 1) % height][i] == "."


def step():
    moved = False
    # naive way: go through the rows
    for j in range(height):
        right = [i for i in range(width) if can_move_right(i, j)]
        moved = moved or bool(right)
        for i in right:
            rows[j][i] = "."
            rows[j][(i + 1) % width] = ">"

    # then go through the columns
    for i in range(width):
        down = [j for j in range(height) if can_move_down(i, j)]
        moved = moved or bool(down)
        for j in down:
            rows[j][i] = "."
            rows[(j + 1) % height][i] = "v"

    return moved


steps = 1
while step():
    steps += 1

print("1:", steps)
