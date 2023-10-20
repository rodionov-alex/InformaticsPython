from itertools import product, permutations

def f(x, y, z, w):
    return (x and (not y)) or (y == z) or (not w)

for x1, x2, x3, x4 in product(range(2), repeat=4):
    t = (
        (x1, x2, 0, 0, 0),
        (1, 0, x3, 0, 0),
        (1, 0, 1, x4, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)

# Ответ: wzyx
