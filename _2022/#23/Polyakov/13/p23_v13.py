# Способ 1
def to_4(n):
    res = ''

    while n != 0:
        res = str(n % 4) + res
        n //= 4

    return int(res)


def f(a, b):
    a4 = to_4(a)

    if a4 == b:
        return 1
    elif a4 > b:
        return 0
    else:
        return f(a + 2, b) + f(a + 3, b) + f(int(str(a4 * 10), 4), b)


print(f(1, 100))


# Способ 2
def f2(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return f2(a + 2, b) + f2(a + 3, b) + f2(a * 4, b)


print(f2(1, int(str(100), 4)))
