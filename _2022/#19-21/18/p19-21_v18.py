def f19(x, p):
    if x >= 1000 or p > 2:
        return p == 2

    if p % 2 == 0:
        return f19(x + 100, p + 1) and f19(x * 2, p + 1)
    else:
        return f19(x + 100, p + 1) or f19(x * 2, p + 1)


def f20(x, p):
    if x >= 1000 or p > 3:
        return p == 3

    if p % 2 == 1:
        return f20(x + 100, p + 1) and f20(x * 2, p + 1)
    else:
        return f20(x + 100, p + 1) or f20(x * 2, p + 1)


# Ваня выйграет на на первый ход (гарантированно + не гарантированно)
def f21_1(x, p):
    if x >= 1000 or p > 2:
        return p == 2

    return f21_1(x + 100, p + 1) or f21_1(x * 2, p + 1)


# Ваня выйграет на свой 1й или второй ход
def f21_2(x, p):
    if x >= 1000 or p > 4:
        return p == 2 or p == 4

    x_sum = f21_2(x + 100, p + 1)
    x_mult = f21_2(x * 2, p + 1)

    if p % 2 == 0:
        return x_sum and x_mult
    else:
        return x_sum or x_mult


res19 = []
res20 = []
res21 = []
res21_1 = []

# Exercise 19
for s in range(1, 1000):
    if f19(s, 0):
        res19.append(s)

print('№19')
print(len(res19))


# Exercise 20
for s in range(1, 1000):
    if f20(s, 0):
        res20.append(s)

print('№20')
print(len(res20))


# Exercise 21
t = []

for s in range(1, 1000):
    if f21_1(s, 0):
        res21_1.append(s)

res21_2 = []

for s in range(1, 1000):
    if f21_2(s, 0):
        res21_2.append(s)

for s in range(1, 1000):
    # Ваня может выйграть как на свой 1й так и 2й ход, но не гарантированно на 1й
    if f21_2(s, 0) and s in res21_1 and s not in res19:
        res21.append(s)

print('№21')
print(min(res21), max(res21))
