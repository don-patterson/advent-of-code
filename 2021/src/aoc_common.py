def load_string(path):
    with open(path) as f:
        return f.read()


def load_lines(path):
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def load_ints(path):
    return [int(line) for line in load_lines(path)]
