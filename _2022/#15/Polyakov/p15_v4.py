# На числовой прямой даны два отрезка: P=[37,60] и Q=[40,77].
# Укажите наименьшую возможную длину такого отрезка A, что формула
# (x ∈ P) → (((x ∈ Q) ∧ (x ∉ A)) → (x ∉ P))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

segments = (37, 60, 40, 77)
p1, p2, q1, q2 = segments

P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
A = []

def f(x):
    return (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))

for x in [i / 10 for i in range((min(segments) + 1) * 10, (max(segments) + 1) * 10)]:
    if not f(x):
        A.append(x)

print(A)

# [40; 60]
# Ответ: 60 - 40 = 20
