def f19(x, p):
    if x >= 43 or p > 2:
        return p == 2 and x <= 72

    if p % 2 == 0:
        return f19(x + 1, p + 1) and f19(x * 2, p + 1) and f19(x * 3, p + 1)
    else:
        return f19(x + 1, p + 1) or f19(x * 2, p + 1) or f19(x * 3, p + 1)


def f20(x, p):
    if x >= 43 or p > 3:
        return (p == 3 and x <= 72) or (p == 2 and x > 72)

    if p % 2 == 1:
        return f20(x + 1, p + 1) and f20(x * 2, p + 1) and f20(x * 3, p + 1)
    else:
        return f20(x + 1, p + 1) or f20(x * 2, p + 1) or f20(x * 3, p + 1)


def f21_1(x, p):
    if x >= 43 or p > 2:
        return (p == 1 and x > 72) or (p == 2 and x <= 72)

    if p % 2 == 0:
        return f21_1(x + 1, p + 1) and f21_1(x * 2, p + 1) and f21_1(x * 3, p + 1)
    else:
        return f21_1(x + 1, p + 1) or f21_1(x * 2, p + 1) or f21_1(x * 3, p + 1)


def f21_2(x, p):
    if x >= 43 or p > 4:
        return (p == 1 and x > 72) or (p == 2 and x <= 72) or (p == 3 and x > 72) or (p == 4 and x <= 72)

    if p % 2 == 0:
        return f21_2(x + 1, p + 1) and f21_2(x * 2, p + 1) and f21_2(x * 3, p + 1)
    else:
        return f21_2(x + 1, p + 1) or f21_2(x * 2, p + 1) or f21_2(x * 3, p + 1)


res19 = []
res20 = []
res21_1 = set()
res21_2 = set()


print("№19")

for s in range(1, 43):
    if f19(s, 0):
        res19.append(s)

print(min(res19))


print("№20")

for s in range(1, 43):
    if f20(s, 0):
        res20.append(s)

print(len(res20))


print("№21")

for s in range(1, 43):
    if f21_1(s, 0):
        res21_1.add(s)

for s in range(1, 43):
    if f21_2(s, 0):
        res21_2.add(s)

res21 = res21_2.difference(res21_1)
print(min(res21), max(res21))
