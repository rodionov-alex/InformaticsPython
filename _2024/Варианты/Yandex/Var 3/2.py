from itertools import product, permutations


def f(x, y, z, w):
    return ((1 == w) == (not ((w and x) or y))) <= z

res = set()

for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 in product(range(2), repeat=10):
    t = ((x1, x2, 1, x3, 0),
         (1, x4, 1, x5, 0),
         (0, 1, 0, 0, 1),
         (1, x6, 1, x7, 1),
         (x8, x9, 1, x10, 1))

    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                res.add(''.join(p))

print(*res)
