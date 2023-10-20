def f(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return f(a + 2, b) + f(a * 2, b)

print(f(1, 16) * f(16, 52))
