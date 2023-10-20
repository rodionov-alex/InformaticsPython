from lib2 import ege_n2

def f(x, y, z, w):
    return (x == (not y)) <= ((z <= (not w)) and (w <= y))

t = (
    (1, 1, 0, 1, 1),
    (0, '*', 0, '*', 0),
    ('*', '*', '*', 0, 0)
)

print(ege_n2(f, 'xyzw', t))
