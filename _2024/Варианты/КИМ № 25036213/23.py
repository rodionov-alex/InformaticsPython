from math import trunc
def f(a, b):
    if a == b:
        return 1
    if a < b or a == 4 or a == 43:
        return 0

    return f(a - 1, b) + f(a // 3, b) + f(trunc(a ** 0.5), b)

print(f(98, 14) * f(14, 2))
