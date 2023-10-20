def f(n):
    if n == 0:
        return 0
    elif 1 <= n < 3:
        return 1
    else:
        return f(n - 1) + f(n - 2)

print(f(47))