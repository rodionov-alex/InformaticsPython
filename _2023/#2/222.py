from lib2 import ege_n2

def f(x, y, z):
    return (x or y) <= (z == x)

t = (
    ('*', 0, 0, 0),
    ('*', 0, '*', 0)
)

print(ege_n2(f, 'xyz', t))