"""
#############
#0123456789T#
###C#B#D#A###
  #B#D#A#C#
  #########
"""

from bisect import insort


edges = {
    "0": {"1"},
    "1": {"0", "2"},
    "2": {"1", "3", "a0"},
    "3": {"2", "4"},
    "4": {"3", "5", "b0"},
    "5": {"4", "6"},
    "6": {"5", "7", "c0"},
    "7": {"6", "8"},
    "8": {"7", "9", "d0"},
    "9": {"8", "10"},
    "10": {"9"},
    "a0": {"2", "a1"},
    "b0": {"4", "b1"},
    "c0": {"6", "c1"},
    "d0": {"8", "d1"},
    "a1": {"a0"},
    "b1": {"b0"},
    "c1": {"c0"},
    "d1": {"d0"},
}
hall = {"0", "1", "3", "5", "7", "9", "10"}
doorways = {"2", "4", "6", "8"}
rooms = {a: {f"{a}{i}" for i in "01"} for a in "abcd"}
cost = {"a": 1, "b": 10, "c": 100, "d": 1000}

# state is a sorted list of (node, piece) tuples


def get_piece(state, node):
    for n, p in state:
        if node == n:
            return p
    return None


def paths_from(*nodes, state):
    end = nodes[-1]
    prev = nodes[-2] if len(nodes) >= 2 else None
    for node in edges[end]:
        if get_piece(state, node) or node == prev:  # if blocked or backtracking
            continue
        yield (*nodes, node)
        yield from paths_from(*nodes, node, state=state)


def moves_from(start, state):
    me = get_piece(state, start)
    my_room = rooms[me]
    is_clean = all(get_piece(state, r) in (None, me) for r in my_room)
    for path in paths_from(start, state=state):
        end = path[-1]
        if start in my_room:
            # in my clean room -- don't leave
            if is_clean:
                if end in my_room:
                    yield end, cost[me] * (len(path) - 1)
            # in my dirty room -- must leave
            else:
                if end in hall:
                    yield end, cost[me] * (len(path) - 1)
        elif start in hall:
            # in the hall -- gotta go to my clean room
            if end in my_room and is_clean:
                yield end, cost[me] * (len(path) - 1)
        else:
            # I'm in another room -- go to the hall or my clean room
            if end in hall or (end in my_room and is_clean):
                yield end, cost[me] * (len(path) - 1)


part1_state = (
    ("a0", "c"),
    ("a1", "b"),
    ("b0", "b"),
    ("b1", "d"),
    ("c0", "d"),
    ("c1", "a"),
    ("d0", "a"),
    ("d1", "c"),
)
finished_state = tuple((r, r[0]) for r, _ in part1_state)


def new_state(state, start, end):
    for node, piece in state:
        if node == end:
            continue
        if node == start:
            yield end, piece
            continue
        yield node, piece


def all_moves_from(state):
    for start, _ in state:
        for end, move_cost in moves_from(start, state=state):
            yield tuple(sorted(new_state(state, start, end))), move_cost


state_cost = {}
exploring = [(part1_state, 0)]


def explore(state, cost_so_far):
    for neighbor_state, neighbor_cost in all_moves_from(state):
        total_cost = cost_so_far + neighbor_cost
        if total_cost < state_cost.get(neighbor_state, 999999):
            state_cost[neighbor_state] = total_cost
            insort(exploring, (neighbor_state, total_cost), key=lambda v: -v[1])


current_state = None
while current_state != finished_state:
    current_state, current_cost = exploring.pop()
    explore(current_state, current_cost)

print("1:", state_cost[finished_state])

"""
#############
#0123456789T#
###C#B#D#A###
  #D#C#B#A#
  #D#B#A#C#
  #B#D#A#C#
  #########
"""
part2_state = (
    ("a0", "c"),
    ("a1", "d"),
    ("a2", "d"),
    ("a3", "b"),
    ("b0", "b"),
    ("b1", "c"),
    ("b2", "b"),
    ("b3", "d"),
    ("c0", "d"),
    ("c1", "b"),
    ("c2", "a"),
    ("c3", "a"),
    ("d0", "a"),
    ("d1", "a"),
    ("d2", "c"),
    ("d3", "c"),
)
finished_state = tuple((r, r[0]) for r, _ in part2_state)

for a in "abcd":
    edges[f"{a}3"] = {f"{a}2"}
    for i in [1, 2]:
        edges[f"{a}{i}"] = {f"{a}{i-1}", f"{a}{i+1}"}
rooms = {a: {f"{a}{i}" for i in "0123"} for a in "abcd"}

state_cost = {}
exploring = [(part2_state, 0)]

current_state = None
while current_state != finished_state:
    current_state, current_cost = exploring.pop()
    explore(current_state, current_cost)

print("2:", state_cost[finished_state])
