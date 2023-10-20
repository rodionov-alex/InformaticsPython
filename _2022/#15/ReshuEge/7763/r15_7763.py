# На числовой прямой даны два отрезка: P = [5, 30] и Q = [14, 23]. Укажите наибольшую возможную длину
# промежутка A, для которого формула
#
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
#
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

p1, p2, q1, q2 = 5, 30, 14, 23

P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

def f(x, A):
    return ((x in P) == (x in Q)) <= (x not in A)

A = set([i / 10 for i in range((min(p1, p2, q1, q2) - 1) * 10, (max(p1, p2, q1, q2) + 1) * 10)])

for x in [i / 10 for i in range((min(p1, p2, q1, q2) - 1) * 10, (max(p1, p2, q1, q2) + 1) * 10)]:
    if not f(x, A):
        A.remove(x)

print(sorted(A))

# [5; 14) и (23; 30]
# 14 - 5 = 9; 30 - 23 = 7
# Ответ: 9