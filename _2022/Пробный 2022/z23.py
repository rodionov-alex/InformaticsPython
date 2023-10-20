def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 2, y) + f(x * 2, y)


print(f(1, 24) * f(24, 50))

# 64