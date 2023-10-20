def f(a, b, c=0):
    if a > b or a == c:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b, c) + f(a + 2, b, c)


v1 = f(11, 17) * f(17, 29, 23)
v2 = f(11, 23, 17) * f(23, 29)
v3 = f(11, 17) * f(17, 23) * f(23, 29)


print(v1 + v2 + v3)
