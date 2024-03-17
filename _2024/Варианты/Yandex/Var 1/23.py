def f(a, b):
    if a > b or a == 81:
        return 0
    if a == b:
        return 1

    return f(a + int(str(a)[0]), b) + f(a + 3, b) + f(2 * a - 1, b)

print(f(42, 73) * f(73, 89))
