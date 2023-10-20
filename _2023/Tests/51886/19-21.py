def f(a, b, p, m):
    if a + b >= 69:
        return p % 2 == m % 2
    if p > m:
        return 0
    h = (f(a + 2, b, p + 1, m), f(a * 2, b, p + 1, m), f(a, b + 2, p + 1, m), f(a, b * 2, p + 1, m))
    return any(h) if (p + 1) % 2 == m % 2 else all(h)


for s in range(1, 64):
    for m in range(1, 5):
        if f(5, s, 0, m):
            #if m == 2:
            print(s, m)
            break

# 19) 16
# 20) 29
# 21) 27 28