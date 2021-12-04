from aoc import lines


def take(n, input):
    for _ in range(n):
        yield next(input)


class Entry:
    def __init__(self, value):
        self.value = int(value)
        self.marked = False

    def __repr__(self):
        return f"{self.value}:{str(self.marked)[0]}"


class Card:
    def __init__(self, *rows):
        self.rows = [[Entry(value) for value in row.split()] for row in rows]

    @property
    def cols(self):
        for i in range(len(self.rows)):
            yield [row[i] for row in self.rows]

    def mark(self, value):
        for row in self.rows:
            for e in row:
                if e.value == value:
                    e.marked = True

    @property
    def winner(self):
        for entries in [*self.rows, *self.cols]:
            if all(e.marked for e in entries):
                return True
        return False

    @property
    def unmarked(self):
        for row in self.rows:
            for entry in row:
                if not entry.marked:
                    yield entry.value


# part 1
input = lines("input-04.txt")
numbers = [int(i) for i in next(input).split(",")]
cards = []

for row in input:
    if row:  # then there should be 4 more
        cards.append(Card(row, *take(4, input)))

first_score = None
last_score = None

for number in numbers:
    for card in cards[:]:
        card.mark(number)
        if card.winner:
            last_score = number * sum(card.unmarked)
            if first_score is None:
                first_score = last_score
            cards.remove(card)

print("1:", first_score)
print("2:", last_score)
