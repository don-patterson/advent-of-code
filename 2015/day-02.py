with open("input/02.txt") as f:
    input = [sorted(int(i) for i in line.split("x")) for line in f]


def area(a, b, c):
    # a < b < c, and area = surface area + a*b
    return 3 * a * b + 2 * b * c + 2 * a * c


def bow(a, b, c):
    # a < b < c
    return 2 * (a + b) + a * b * c


print("1:", sum(area(*abc) for abc in input))
print("2:", sum(bow(*abc) for abc in input))
