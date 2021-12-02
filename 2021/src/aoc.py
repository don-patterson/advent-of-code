def apply(calls, args):
    for call, arg in zip(calls, args, strict=True):
        yield call(arg)


def lines(path, *, shape=str):
    if callable(shape):
        cast_line = shape
    else:
        cast_line = lambda line: [*apply(calls=shape, args=line.split())]

    with open(path) as f:
        for line in f:
            yield cast_line(line.strip())
