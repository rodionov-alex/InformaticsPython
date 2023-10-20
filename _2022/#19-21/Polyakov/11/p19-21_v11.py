def f19(x, p):
    if x >= 65 or p > 2:
        return p == 2

    if p % 2 == 0:
        return f19(x + 1, p + 1) and f19(x + 2, p + 1) and f19(x * 3, p + 1)
    else:
        return f19(x + 1, p + 1) or f19(x + 2, p + 1) or f19(x * 3, p + 1)


def f20(x, p):
    if x >= 65 or p > 3:
        return p == 3

    if p % 2 == 1:
        return f20(x + 1, p + 1) and f20(x + 2, p + 1) and f20(x * 3, p + 1)
    else:
        return f20(x + 1, p + 1) or f20(x + 2, p + 1) or f20(x * 3, p + 1)


def f21(x, p):
    if x >= 65 or p > 4:
        return p == 2 or p == 4

    if p % 2 == 0:
        return f21(x + 1, p + 1) and f21(x + 2, p + 1) and f21(x * 3, p + 1)
    else:
        return f21(x + 1, p + 1) or f21(x + 2, p + 1) or f21(x * 3, p + 1)


res19 = []
res20 = []
res21 = []

# Exercise 19
for s in range(1, 65):
    if f19(s, 0):
        res19.append(s)

print('№19')
print(res19)


# Exercise 20
for s in range(1, 65):
    if f20(s, 0):
        res20.append(s)

print('№20')
print(min(res20), max(res20))


# Exercise 21
for s in range(1, 65):
    if f21(s, 0):
        res21.append(s)

print('№21')
print(min(res21))
