"""
I want to make a symbolic math class for simple operations like
addition, multiplication, and mod. I wonder how hard that would be...

It should handle all of the operations in the ALU from 2021-24. That is,
"add", "mul", "div", "mod", and "eql"

The full block of ALU commands looks like:
    inp w
    mul x 0
    add x z
    mod x 26
    div z 26
    add x -10
    eql x w
    eql x 0
    mul y 0
    add y 25
    mul y x
    add y 1
    mul z y
    mul y 0
    add y w
    add y 13
    mul y x
    add z y

Read 2021/24 for more info.
"""


from collections import Counter
import collections
from collections.abc import Sequence


class Polynomial:
    """
    Holds amounts like 3*x + 4.

    You specify a dictionary of power:coefficient terms:
      - {2:5, 1:2, 0:-17}  -->   5x^2 + 2x - 17
      - {100:-4, 4:2}      -->   -4x^100 + 2x*4
    """

    def __init__(self, **kw):
        self.variable = kw.get("variable", "x")
        self.terms = Counter(kw.get("terms", {}))
        self._compact()

    def _compact(self):
        # do we ever want to mutate like this?  ... do we ever not want to?
        for k in list(k for k, v in self.terms.items() if v == 0):
            del self.terms[k]

    def _sign(self, term):
        return "+" if term[1] >= 0 else "-"

    @staticmethod
    def _split(self, term):
        power, coefficient = term
        sign = "-" if coefficient < 0 else "+"
        number = abs(coefficient)
        symbol = "" if power == 0 else f"{self.variable}^{power}"

        return sign, f"{number}{symbol}"

    def __repr__(self):
        leading, *remaining = sorted(self.terms.items(), reverse=True) or [(0, 0)]
        pieces = []

        # leading term needs its sign
        sign, value = self._split(leading)
        pieces.append(value if sign == "+" else f"-{value}")

        for term in remaining:
            sign, value = self._split(term)
            pieces.append(f"{sign} {value}")

        return "".join(pieces)

    def __add__(self, other):
        if isinstance(other, int):
            return Polynomial(
                variable=self.variable,
                coefficients=self.coefficients + Counter({0: other}),
            )
        if isinstance(other, Polynomial) and self.variable == other.variable:
            return Polynomial(
                variable=self.variable,
                coefficients=self.coefficients + other.coefficients,
            )
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Polynomial(
                variable=self.variable,
                coefficients=Counter(
                    {k: v * other for k, v in self.coefficients.items()}
                ),
            )
        return NotImplemented

    @staticmethod
    def _div_to_0(a, b):
        return -(-a // b) if (a < 0) ^ (b < 0) else a // b

    def __truediv__(self, other):
        return NotImplemented


def tests():
    q = Polynomial(terms={5: 2, 8: -5, 0: 44})
    print(q)
    print(q + 10)
    print(q * 5)

    r = Polynomial("x", multiplier=25, constant=-33)
    print(r)
    print(q + r)
    print(r / 26)


tests()
