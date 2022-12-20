sample = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""
rates = {}
edges = {}
with open("input/16.txt") as f:
    for line in f:
        _, node, _, _, rate, _, _, _, _, exits = line.split(maxsplit=9)
        rates[node] = int(rate[5:-1])
        edges[node] = exits.strip().split(", ")

valves = {n for n, r in rates.items() if r > 0}
valve_to_int = {valve: 2**i for i, valve in enumerate(sorted(valves))}


def valve_code(open_valves):
    return sum(valve_to_int[v] for v in open_valves)


_value_cache = {}  # key=(position, time, valve_code)


def value(position, time, valve_code):
    if time == 1:
        return 0

    if (cached := _value_cache.get((position, time, valve_code))) is not None:
        return cached

    total = 0
    # if (position should be openend) and (isn't already opened)
    if rates[position] > 0 and not valve_to_int[position] & valve_code:
        total = max(
            total,
            value(position, time - 1, valve_to_int[position] + valve_code)
            + (time - 1) * rates[position],
        )

    # all moves
    total = max(
        total,
        max(value(neighbor, time - 1, valve_code) for neighbor in edges[position]),
    )

    _value_cache[(position, time, valve_code)] = total
    return total


print("1:", value("AA", 30, 0))
