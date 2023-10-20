def f19(x1, x2, p):
    if x1 + x2 >= 223 or p > 2:
        return p == 2

    return f19(x1 + 1, x2, p + 1) or f19(x1, x2 + 1, p + 1) or \
           f19(x1 * 2, x2, p + 1) or f19(x1, x2 * 2, p + 1)


def f20(x1, x2, p):
    if x1 + x2 >= 223 or p > 3:
        return p == 3

    if p % 2:
        return f20(x1 + 1, x2, p + 1) and f20(x1, x2 + 1, p + 1) and \
               f20(x1 * 2, x2, p + 1) and f20(x1, x2 * 2, p + 1)
    else:
        return f20(x1 + 1, x2, p + 1) or f20(x1, x2 + 1, p + 1) or \
               f20(x1 * 2, x2, p + 1) or f20(x1, x2 * 2, p + 1)


def f21(x1, x2, p):
    if x1 + x2 >= 223 or p > 4:
        return p % 2 == 0

    if p % 2 == 0:
        return f21(x1 + 1, x2, p + 1) and f21(x1, x2 + 1, p + 1) and \
               f21(x1 * 2, x2, p + 1) and f21(x1, x2 * 2, p + 1)
    else:
        return f21(x1 + 1, x2, p + 1) or f21(x1, x2 + 1, p + 1) or \
               f21(x1 * 2, x2, p + 1) or f21(x1, x2 * 2, p + 1)


res19 = []
res20 = []
res21 = []

for s in range(1, 206):
    if f19(17, s, 0):
        res19.append(s)

print(min(res19))

for s in range(1, 206):
    if f20(17, s, 0):
        res20.append(s)

print(res20)

for s in range(1, 206):
    if f21(17, s, 0):
        res21.append(s)

print(min(res21))
