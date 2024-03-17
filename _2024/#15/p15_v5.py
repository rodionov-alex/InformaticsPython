"""
На числовой прямой даны три отрезка: P = [131; 215], Q = [36; 384] и R = [243; 355].
Укажите наименьшую возможную длину такого отрезка A, что формула
(¬((x ∈ Q) → ((x ∈ P) ∨ (x ∈ R)))) → (¬(x ∈ A) → ¬(x ∈ Q))
тождественно истинна, то есть принимает значение 1 при любом значении переменной х?

Ответ: 348
"""

# region Способ 1
data = [131, 215, 36, 384, 243, 355]
longest = 0
value = 1

for x in [i / 4 for i in range(min(data) * 4, max(data) * 4 + 1)]:
    P = 131 <= x <= 215
    Q = 36 <= x <= 384
    R = 243 <= x <= 355
    A = longest

    f = (not (Q <= (P or R))) <= ((not A) <= (not Q))

    if f != ((not longest) == value):
        print(x)
# endregion

# region Способ 2
p1, p2, q1, q2, r1, r2 = 131, 215, 36, 384, 243, 355

P = {i / 10 for i in range(p1 * 10, p2 * 10 + 1)}
Q = {i / 10 for i in range(q1 * 10, q2 * 10 + 1)}
R = {i / 10 for i in range(r1 * 10, r2 * 10 + 1)}

A = []


def f(x):
    return (not ((x in Q) <= ((x in P) or (x in R)))) <= ((not (x in A)) <= (not (x in Q)))


for x in [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]:
    if not f(x):
        A.append(x)

print(A)
begin = 0

# Проверка на разрывы
for i in range(1, len(A)):
    if round(A[i] - A[i - 1], 1) > 0.1:
        print("[{}; {}] Длина {}".format(A[begin], A[i - 1], round(A[i - 1]) - round(A[begin])))
        begin = i

print("[{}; {}] Длина {}".format(A[begin], A[-1], round(A[-1]) - round(A[begin])))
# endregion

# [36; 131)
# (215; 243)
# (355; 384]

# Проверка
A = [i for i in range(36, 384 + 1)]
res = []
for x in range(500):
    if not f(x):
        res.append(x)
print(res)

print(384 - 36)
