def f(n):
    if n < 3:
        return 2
    else:
        if n % 2:
            return f(n - 2) - f(n - 1) + 2 * n
        else:
            return f(n - 1) + f(n - 2) - n


print(f(30))