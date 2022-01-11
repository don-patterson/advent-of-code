from re import findall, search

with open("input/05.txt") as f:
    input = f.readlines()


def requirements(word):
    yield not search(pattern="ab|cd|pq|xy", string=word)
    yield len(findall(pattern="[aeiou]", string=word)) >= 3
    yield search(pattern=r"(.)\1", string=word)


def nice(word):
    return all(requirements(word))


print("1:", sum(1 for word in input if nice(word)))


def requirements2(word):
    yield search(pattern=r"(..).*\1", string=word)
    yield search(pattern=r"(.).\1", string=word)


def nice2(word):
    return all(requirements2(word))


print("2:", sum(1 for word in input if nice2(word)))
