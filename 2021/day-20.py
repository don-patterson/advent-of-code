def input():
    with open("input-20.txt") as lines:
        for line in lines:
            yield line.strip()


input = input()
enhancer = next(input)
assert len(enhancer) == 512
assert next(input) == ""
pixels = {(x, y): c for y, row in enumerate(input) for x, c in enumerate(row)}


class Image:
    def __init__(self, pixels, outside=".", enhancer=enhancer):
        self.pixels = pixels
        self.outside = outside
        self.enhancer = enhancer
        self.calculate_bounds()

    def calculate_bounds(self):
        left = right = top = bottom = 0
        for (x, y) in self.pixels:
            if x < left:
                left = x
            if x > right:
                right = x
            if y < top:
                top = y
            if y > bottom:
                bottom = y
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def glyph(self, x, y):
        return self.pixels.get((x, y), self.outside)

    def plot(self, border=5):
        for y in range(self.top - border, self.bottom + border + 1):
            for x in range(self.left - border, self.right + border + 1):
                print(self.glyph(x, y), end="")
            print()

    def index(self, x, y):
        b = []
        for j in (-1, 0, 1):
            for i in (-1, 0, 1):
                b.append("1" if self.glyph(x + i, y + j) == "#" else "0")
        return int("".join(b), 2)

    def enhance(self):
        """mutates this image"""
        enhanced = {}
        for y in range(self.top - 1, self.bottom + 2):
            for x in range(self.left - 1, self.right + 2):
                enhanced[(x, y)] = self.enhancer[self.index(x, y)]
        self.pixels = enhanced
        self.calculate_bounds()
        self.outside = self.enhancer[self.index(self.left - 5, 0)]


image = Image(pixels)
image.enhance()
image.enhance()
# image.plot()
# print(" ^outside:", image.outside)

print("1:", sum(1 for v in image.pixels.values() if v == "#"))
for _ in range(48):
    image.enhance()
print("2:", sum(1 for v in image.pixels.values() if v == "#"))
