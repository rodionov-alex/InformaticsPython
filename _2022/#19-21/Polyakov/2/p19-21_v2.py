# Exercise 19
def f19(x, p):
    if x >= 65 or p > 2:
        return x <= 100 and p == 2

    return f19(x + 1, p + 1) or f19(x * 3, p + 1)


res19 = []

for s in range(1, 65):
    if f19(s, 0):
        res19.append(s)

print('№19')
print(min(res19))


# Exercise 20
def f20(x, p):
    if x >= 65 or p > 3:
        return (p == 3 and x <= 100) or (p == 2 and x > 100)

    if p % 2 == 0:
        return f20(x + 1, p + 1) or f20(x * 3, p + 1)
    else:
        return f20(x + 1, p + 1) and f20(x * 3, p + 1)


res20 = []

for s in range(1, 65):
    if f20(s, 0):
        res20.append(s)

print('№20')
print(res20)


# Exercise 21
def f21(x, p):
    if x >= 65 or p > 4:
        return ((p == 2 or p == 4) and x <= 100) or \
               ((p == 1 or p == 3) and x > 100)

    if p % 2 == 0:
        return f21(x + 1, p + 1) and f21(x * 3, p + 1)
    else:
        return f21(x + 1, p + 1) or f21(x * 3, p + 1)


res21 = []

for s in range(1, 65):
    if f21(s, 0):
        res21.append(s)

print('№21')
print(min(res21))
