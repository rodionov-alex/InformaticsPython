from itertools import *
def f(p, y, h, n):
    return y and (not (y or h)) or (not (y <= h)) and (n <= p)

for x1, x2, x3, x4, x5, x6 in product((0, 1), repeat=6):
    t = (
        (x1, x2, x4, 1, 1),
        (x4, 1, x5, 1, 1),
        (x6, 1, 1, 1, 1),
    )

    if len(t) == len(set(t)):
        for p in permutations('pyhn'):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)