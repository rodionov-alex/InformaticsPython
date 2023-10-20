import lib2

def f(a, b, c, d):
    return a and (not b) or (a or b) and c or d

t = (
    ('*', '*', '*', 1, 0),
    ('*', 1, '*', 1, 0),
    (1, '*', '*', '*', 0),
)

print(lib2.ege_n2(f, 'abcd', t))