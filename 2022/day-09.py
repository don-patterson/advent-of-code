with open("input/09.txt") as f:
    moves = [line.split() for line in f]

pos = {"H": (0, 0), "T": (0, 0)}
directions = {
    "L": (-1, 0),
    "R": (+1, 0),
    "U": (0, +1),
    "D": (0, -1),
}


def move(piece, direction):
    x, y = pos[piece]
    dx, dy = direction
    pos[piece] = (x + dx, y + dy)


def catch_up(head, tail):
    hx, hy = pos[head]
    tx, ty = pos[tail]
    dx = hx - tx
    dy = hy - ty

    if max(abs(dx), abs(dy)) <= 1:
        return

    if abs(dx) == 2:
        dx //= 2
    if abs(dy) == 2:
        dy //= 2

    move(tail, (dx, dy))


history = set()
for d, count in moves:
    for _ in range(int(count)):
        move("H", directions[d])
        catch_up("H", "T")
        history.add(pos["T"])
print("1:", len(history))


pos = {k: (0, 0) for k in range(10)}
history = set()
for d, count in moves:
    for _ in range(int(count)):
        move(0, directions[d])
        for i in range(9):
            catch_up(i, i + 1)
        history.add(pos[9])
print("2:", len(history))
