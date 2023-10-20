def g(n):
    if n % 2 == 0:
        return n + 1
    else:
        return n + 2


def f(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return f(a + 1, b) + f(a * 2, b) + f(g(a), b)


print(f(3, 9) * f(9, 17) * f(17, 25))
