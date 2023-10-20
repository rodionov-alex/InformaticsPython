from itertools import product
from itertools import permutations

def f(x, y, z, w):
    return (x and (not y)) or (y == z) or (not w)

for x1, x2, x3, x4 in product((0, 1), repeat=4):
    t = (
        (0, x1, x2, 0, 0),
        (0, 1, 0, 1, 0),
        (x3, 1, 0, x4, 0),
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)

