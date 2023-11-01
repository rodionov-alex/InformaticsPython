
def f19(x, p, t):
    if x == 1 and p == t:
        return True
    else:
        if x > 1 and p == t:
            return False
        else:
            if x < 1:
                return False

    if x % 2 == 0:
        x1 = x // 2
    else:
        x1 = x - 2

    if x % 3 == 0:
        x2 = x // 3
    else:
        x2 = x - 3

    return f19(x1, p + 1, t) or f19(x2, p + 1, t)


res19 = []

for s in range(1, 38):
    if f19(s, 0, 1) and f19(s, 0, 2):
        res19.append(s)

print('№19')
print(max(res19))


# Exercise 20
def f20(x, p):
    if x == 1 and p == 3:
        return True
    else:
        if x > 1 and p == 3:
            return False
        else:
            if x < 1:
                return False

    if x % 2 == 0:
        x1 = x // 2
    else:
        x1 = x - 2

    if x % 3 == 0:
        x2 = x // 3
    else:
        x2 = x - 3

    if p % 2 == 1:
        return f20(x1, p + 1) and f20(x2, p + 1)
    else:
        return f20(x1, p + 1) or f20(x2, p + 1)


res20 = []

for s in range(1, 38):
    if f20(s, 0):
        res20.append(s)

print('№20')
print(min(res20), max(res20))


# Exercise 21
def f21(x, p, t):
    if x == 1 and p == t:
        return True
    else:
        if x > 1 and p == t:
            return False
        else:
            if x < 1:
                return False

    if x % 2 == 0:
        x1 = x // 2
    else:
        x1 = x - 2

    if x % 3 == 0:
        x2 = x // 3
    else:
        x2 = x - 3

    return f21(x1, p + 1, t) or f21(x2, p + 1, t)


res21 = []

for s in range(1, 38):
    if f21(s, 0, 2) and f21(s, 0, 4):
        res21.append(s)

print('№21')
print(min(res21))
