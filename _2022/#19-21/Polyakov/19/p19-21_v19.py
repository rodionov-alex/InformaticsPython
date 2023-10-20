win = 73

def f19(x1, x2, x3, p, t):
    if x1 + x2 + x3 >= win or p > t:
        return p == t
    return f19(x1 + 3, x2, x3, p + 1, t) or f19(x1 + 13, x2, x3, p + 1, t) or f19(x1 + 23, x2, x3, p + 1, t) or \
           f19(x1, x2 + 3, x3, p + 1, t) or f19(x1, x2 + 13, x3, p + 1, t) or f19(x1, x2 + 23, x3, p + 1, t) or \
           f19(x1, x2, x3 + 3, p + 1, t) or f19(x1, x2, x3 + 13, p + 1, t) or f19(x1, x2, x3 + 23, p + 1, t)

r19 = []

for s in range(1, 24):
    if f19(2, s, s*2, 0, 2):
        r19.append(s)

print(min(r19))

def f20(x1, x2, x3, p, t):
    if x1 + x2 + x3 >= win or p > t:
        return p == t
    if p % 2 == 1:
        return f20(x1 + 3, x2, x3, p + 1, t) and f20(x1 + 13, x2, x3, p + 1, t) and f20(x1 + 23, x2, x3, p + 1, t) and \
           f20(x1, x2 + 3, x3, p + 1, t) and f20(x1, x2 + 13, x3, p + 1, t) and f20(x1, x2 + 23, x3, p + 1, t) and \
           f20(x1, x2, x3 + 3, p + 1, t) and f20(x1, x2, x3 + 13, p + 1, t) and f20(x1, x2, x3 + 23, p + 1, t)
    else:
        return f20(x1 + 3, x2, x3, p + 1, t) or f20(x1 + 13, x2, x3, p + 1, t) or f20(x1 + 23, x2, x3, p + 1, t) or \
           f20(x1, x2 + 3, x3, p + 1, t) or f20(x1, x2 + 13, x3, p + 1, t) or f20(x1, x2 + 23, x3, p + 1, t) or \
           f20(x1, x2, x3 + 3, p + 1, t) or f20(x1, x2, x3 + 13, p + 1, t) or f20(x1, x2, x3 + 23, p + 1, t)

r20 = []

for s in range(1, 24):
    if f20(2, s, s*2, 0, 3):
        r20.append(s)

print(min(r20), max(r20))

def f21(x1, x2, x3, p, t):
    if x1 + x2 + x3 >= win or p > t:
        return p % 2 == 0
    if p % 2 == 0:
        return f21(x1 + 3, x2, x3, p + 1, t) and f21(x1 + 13, x2, x3, p + 1, t) and f21(x1 + 23, x2, x3, p + 1, t) and \
           f21(x1, x2 + 3, x3, p + 1, t) and f21(x1, x2 + 13, x3, p + 1, t) and f21(x1, x2 + 23, x3, p + 1, t) and \
           f21(x1, x2, x3 + 3, p + 1, t) and f21(x1, x2, x3 + 13, p + 1, t) and f21(x1, x2, x3 + 23, p + 1, t)
    else:
        return f21(x1 + 3, x2, x3, p + 1, t) or f21(x1 + 13, x2, x3, p + 1, t) or f21(x1 + 23, x2, x3, p + 1, t) or \
           f21(x1, x2 + 3, x3, p + 1, t) or f21(x1, x2 + 13, x3, p + 1, t) or f21(x1, x2 + 23, x3, p + 1, t) or \
           f21(x1, x2, x3 + 3, p + 1, t) or f21(x1, x2, x3 + 13, p + 1, t) or f21(x1, x2, x3 + 23, p + 1, t)

r21 = []
r21_2 = []

for s in range(1, 24):
    if f21(2, s, s*2, 0, 4) and s in r19 and not f21(2, s, s*2, 0, 2):
        r21.append(s)

print(r21)