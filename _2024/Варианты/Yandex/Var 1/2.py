def f(a, b, c, d):
    return (a <= b) and (b <= c) and (c <= d)

from itertools import product, permutations

for x1, x2 in product((0, 1), repeat=2):
    t = (
        (0, x1, 1, 0, 1),
        (0, x2, 1, 0, 1),
        (0,  1, 1, 1, 1)
    )

    if len(t) == len(set(t)):
        for p in permutations('abcd'):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
