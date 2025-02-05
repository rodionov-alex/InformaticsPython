# На числовой прямой даны два отрезка: P=[4,15] и Q=[12,20].
# Укажите наименьшую возможную длину такого отрезка A, что формула
# ((x ∈ P) ∧ (x ∈ Q)) → (x ∈ A)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

p1, p2, q1, q2 = 4, 15, 12, 20

P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
A = []

def f(x):
    return ((x in P) and (x in Q)) <= (x in A)

for x in [i / 10 for i in range(3 * 10, 21 * 10)]:
    if not f(x):
        A.append(x)

print(A)

# [12, 15]
# Ответ: 15 - 12 = 3
