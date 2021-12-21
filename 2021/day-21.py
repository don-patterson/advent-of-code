from itertools import cycle, product
from collections import Counter

d100 = cycle(range(1, 100 + 1))


def roll(n=3):
    return sum(next(d100) for _ in range(n))


def move(position, distance):
    return (position + distance - 1) % 10 + 1


p1, s1 = 10, 0
p2, s2 = 2, 0
rolls = 0

while True:
    p1 = move(p1, roll())
    s1 += p1
    rolls += 3

    if s1 >= 1000:
        break

    p2 = move(p2, roll())
    s2 += p2
    rolls += 3

    if s2 >= 1000:
        break

# spoiler, p1 won:
print("1:", s2 * rolls)


class Game:
    def __init__(self, p1, s1, p2, s2, rolls):
        self.p1 = p1
        self.s1 = s1
        self.p2 = p2
        self.s2 = s2
        self.rolls = rolls

    @property
    def state(self):
        return (self.p1, self.s1, self.p2, self.s2, self.rolls)

    @property
    def winner(self):
        if self.s1 >= 21:
            return "p1"
        if self.s2 >= 21:
            return "p2"
        return None

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.state == other.state

    def split(self):
        # generates 27 copies!
        p1, s1, p2, s2, rolls = self.state
        if rolls % 2 == 0:  # p1's turn
            for dice in product((1, 2, 3), repeat=3):
                next_p1 = move(p1, sum(dice))
                yield Game(next_p1, s1 + next_p1, p2, s2, rolls + 3)
        else:
            for dice in product((1, 2, 3), repeat=3):
                next_p2 = move(p2, sum(dice))
                yield Game(p1, s1, next_p2, s2 + next_p2, rolls + 3)

    def __repr__(self) -> str:
        return f"Game{self.state}"


games = Counter({Game(10, 0, 2, 0, 0): 1})
wins = {"p1": 0, "p2": 0}
while games:
    new_games = Counter()
    for game, count in games.items():
        for split_game, split_count in Counter(game.split()).items():
            if winner := split_game.winner:
                wins[winner] += count * split_count
            else:
                new_games[split_game] += count * split_count
    games = new_games

print("2:", max(wins.values()))
