"""
На числовой прямой даны три отрезка: P = [1023; 2148], Q = [1362; 3898] и R = [1813; 2566].
Укажите наименьшую возможную длину такого отрезка A, что формула
(¬((x ∈ Q) → ((x ∈ P) ∨ (x ∈ R)))) → (¬(x ∈ A) → ¬(x ∈ Q))
тождественно истинна, то есть принимает значение 1 при любом значении переменной х?

Ответ:
"""

# region Способ 1
data = [1023, 2148, 1362, 3898, 1813, 2566]
k = 4
longest = 0
value = 1

for x in [i / k for i in range(min(data) * k, max(data) * k + 1)]:
    P = 1023 <= x <= 2148
    Q = 1362 <= x <= 3898
    R = 1813 <= x <= 2566
    A = longest

    f = (not (Q <= (P or R))) <= ((not A) <= (not Q))

    if f != ((not longest) == value):
        print(x)
# endregion

# region Способ 2
p1, p2, q1, q2, r1, r2 = 1023, 2148, 1362, 3898, 1813, 2566

P = {i / 10 for i in range(p1 * 10, p2 * 10 + 1)}
Q = {i / 10 for i in range(q1 * 10, q2 * 10 + 1)}
R = {i / 10 for i in range(r1 * 10, r2 * 10 + 1)}
A = []

def f(x):
    return (not ((x in Q) <= ((x in P) or (x in R)))) <= ((not (x in A)) <= (not (x in Q)))

for x in [i / 10 for i in range(p1 * 10, q2 * 10 + 1)]:
    if not f(x):
        A.append(x)

# print(A)
begin = 0

# Проверка на разрывы
for i in range(1, len(A)):
    if round(A[i] - A[i - 1], 1) > 0.1:
        print("[{}; {}] Длина {}".format(A[begin], A[i - 1], round(A[i - 1]) - round(A[begin])))
        begin = i

print("[{}; {}] Длина {}".format(A[begin], A[i - 1], round(A[i]) - round(A[begin])))
# endregion
