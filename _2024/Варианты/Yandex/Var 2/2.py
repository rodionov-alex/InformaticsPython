from itertools import product, permutations

def f(a, b, c, d):
    return ((a and b) <= c) and ((b and c) <= d)


for x1, x2, x3, x4, x5, x6 in product(range(2), repeat=6):
    t = (
        (x1, 1, 1, 1, 0),
        (x2, 1, x3, 1, 0),
        (1, 1, 1, x4, 0),
        (x5, 1, 1, x6, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('abcd'):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
