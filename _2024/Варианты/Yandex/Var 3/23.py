def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a - int(str(a ** 2)[0]), b) + f(a - sum(map(int, str(a))), b)

print(f(32, 1))