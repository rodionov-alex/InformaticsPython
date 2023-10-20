import lib2

def f(x, y, z, w):
    return (y or x) == (y <= w) or (not z)

t = (
    (1, 0, 0, 0, 0),
    (1, 1, 0, 0, 0),
    (1, 0, 1, 0, 0),
)

print(lib2.ege_n2(f, 'xyzw', t))