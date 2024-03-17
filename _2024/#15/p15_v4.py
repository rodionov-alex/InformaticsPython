"""
На числовой прямой даны три отрезка: P = [1381; 2165], Q = [369; 3894] и R = [2643; 3155].
Укажите наименьшую возможную длину такого отрезка A, что формула

(¬((x ∈ Q) → ((x ∈ P) ∨ (x ∈ R)))) → (¬(x ∈ A) → ¬(x ∈ Q))

тождественно истинна, то есть принимает значение 1 при любом значении переменной х?

Ответ: 3525
"""

p1, p2, q1, q2, r1, r2 = 1381, 2165, 369, 3894, 2643, 3155

P = {i / 10 for i in range(p1 * 10, p2 * 10 + 1)}
Q = {i / 10 for i in range(q1 * 10, q2 * 10 + 1)}
R = {i / 10 for i in range(r1 * 10, r2 * 10 + 1)}

A = {i / 10 for i in range(q1 * 10, q2 * 10 + 1)}


def f(x):
    return (not ((x in Q) <= ((x in P) or (x in R)))) <= ((x not in A) <= (x not in Q))


for x in [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]:
    if not f(x):
        A.remove(x)

A = sorted(A)
print(A)
begin = 0

# Проверка на разрывы
for i in range(1, len(A)):
    if round(A[i] - A[i - 1], 1) > 0.1:
        print("[{}; {}] Длина {}".format(A[begin], A[i - 1], round(A[i - 1]) - round(A[begin])))
        begin = i

print("[{}; {}] Длина {}".format(A[begin], A[i - 1], round(A[i]) - round(A[begin])))
