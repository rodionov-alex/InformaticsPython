def f(a, b, p, m):
    if a + b >= 88:
        return p % 2 == m % 2
    elif p == m:
        return 0
    h = [f(a + 1, b, p + 1, m), f(a, b + 1, p + 1, m), f(a * 3, b, p + 1, m), f(a, b * 3, p + 1, m)]
    return any(h) if (p + 1) % 2 == m % 2 else all(h) # any(h)

for s in range(1, 82):
    for m in range(1, 5):
        if f(6, s, 0, m):
            if m == 2 or m == 4:
                print(s, m)
                break
