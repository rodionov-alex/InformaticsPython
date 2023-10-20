# Способ 1
def to_3(n):
    res = ''

    while n != 0:
        res = str(n % 3) + res
        n //= 3

    return int(res)


def to_10(n):
    return int(str(n), 3)


def f(a, b):
    if a == b:
        return 1
    elif a < b:
        return 0
    elif a % 10 == 0:  # Если последняя цифра уже ноль, то второе действие бессмысленно
        return f(to_3(to_10(a) - 2), b)
    else:
        return f(to_3(to_10(a) - 2), b) + f(a // 10 * 10, b)


print(f(212, 10))


# Способ 2
def f2(a, b):
    if a == b:
        return 1
    elif a < b:
        return 0
    elif a % 3 == 0:  # Если последняя цифра уже ноль, то второе действие бессмысленно
        return f2(a - 2, b)
    else:
        return f2(a - 2, b) + f2(a - a % 3, b)


print(f2(int(str(212), 3), int(str(10), 3)))
