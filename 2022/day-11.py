from re import findall

monkies = []
with open("input/11.txt") as f:
    for line in f:
        if not line.startswith("Monkey"):
            continue
        monkey = {
            "count": 0,
            "n": findall("\d+", line)[0],
            "items": [int(i) for i in findall("\d+", next(f))],
            "op": eval("lambda old:" + next(f).split("=")[1]),
            "test": int(next(f).split()[-1]),
            "target1": int(next(f).split()[-1]),
            "target2": int(next(f).split()[-1]),
        }
        monkies.append(monkey)


def turn1(monkey):
    for item in monkey["items"]:
        monkey["count"] += 1
        worry = monkey["op"](item) // 3
        target = monkey["target1"] if worry % monkey["test"] == 0 else monkey["target2"]
        monkies[target]["items"].append(worry)
    monkey["items"].clear()


for i in range(20):
    for m in monkies:
        turn1(m)

m1, m2 = sorted(m["count"] for m in monkies)[-2:]
print("1:", m1 * m2)
