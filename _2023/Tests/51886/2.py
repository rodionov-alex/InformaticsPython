from itertools import product, permutations

def f(a, b, c , d):
    return ((not a) <= b) and (b == (not c)) and (not d)

for x1, x2, x3, x4, x5, x6, x7 in product((0, 1), repeat=7):
    t = (
        (1, x1, x2, x3, 1),
        (1,  1, x4, x5, 1),
        (x6, 1, 1,  x7, 1)
    )

    if len(t) == len(set(t)):
        for p in permutations('abcd', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
