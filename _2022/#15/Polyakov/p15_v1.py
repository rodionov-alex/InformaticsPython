# На числовой прямой даны два отрезка: P=[10,29] и Q=[13,18].
# Укажите наибольшую возможную длину такого отрезка A, что формула
# ((x ∈ A) → (x ∈ P)) ∨ (x ∈ Q)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

p1, p2, q1, q2 = 10, 29, 13, 18

P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

def f(x, A):
    return ((x in A) <= (x in P)) or (x in Q)

A = set([i / 10 for i in range(9 * 10, 30 * 10)])

for x in [i / 10 for i in range(9 * 10, 30 * 10)]:
    if not f(x, A):
        A.remove(x)

print(sorted(A))

# [10, 29]
# Ответ: 29 - 10 = 19