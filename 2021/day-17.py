"""       .
|     .       .
|   .           .
| .
S                 .
|
|                  .
|               ===  -69 ===
|           211|   target   |232
|               === -124 ===
"""

from typing import NamedTuple

x_min, x_max = 211, 232
y_min, y_max = -124, -69


class vec(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return vec(self.x + other.x, self.y + other.y)


g = vec(x=0, y=-1)
g_drag = vec(x=-1, y=-1)


def step(p0: vec, v0: vec):
    p1 = p0 + v0
    v1 = v0 + (g_drag if v0.x > 0 else g)
    return p1, v1


def hit(p: vec):
    return x_min <= p.x <= x_max and y_min <= p.y <= y_max


def too_far(p: vec, v: vec):
    return (
        # 1. you flew by in the x direction
        p.x > x_max
        or
        # 2. you flew by in the y direction
        (p.y < y_min and v.y <= 0)
    )


# find the smallest feasible x velocity. any less than this and you just won't make it
def total_x_distance(vx):  # i.e. sum(vx, vx-1, vx-2, ..., 2, 1)
    return (vx * (vx + 1)) // 2


vx = 1
while total_x_distance(vx) < x_min:
    vx += 1

vx_min = vx
vx_max = x_max  # i.e. any larger and you'll skip in on step 1


# can you find bounds for y as well?

# well, if vy < -124 then the first step you'll be below the target.
# if y_min was positive this would be need to be calculated
vy_min = y_min

# and you always go up up up, hit a peak (vy = 0 for 1 step, so you repeat the peak)
# and then come down symmetrically. so you always hit 0 with a velocity of -(initial+1)
#
#  6            0up  1down
#  5        1up         2down
#  3    2up                3down
#  0 3up ------------------- 4down
# -4                           here
#
# so if vy > 124 then you'll never hit a value in [0, -124]
# again, if y_min was positive this would be a different story.
vy_max = -y_min


def max_y_height(vy):
    if vy < 0:
        return vy
    return (vy * (vy + 1)) // 2


def shoot(v0: vec):
    p = vec(0, 0)
    v = v0

    while True:
        p, v = step(p, v)
        if hit(p):
            return True
        if too_far(p, v):
            return False


# try em all?
def fire_away():
    for vx in range(vx_min, vx_max + 1):
        for vy in range(vy_min, vy_max + 1):
            if shoot(vec(vx, vy)):
                yield vx, vy


print("1:", max(max_y_height(vy) for _, vy in fire_away()))
print("2:", sum(1 for _ in fire_away()))
