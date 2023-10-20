# На числовой прямой даны три отрезка: P=[10,25], Q=[15,30] и R=[25,40].
# Какова максимальная длина отрезка A, при котором формула
# ((x ∈ Q) → (x ∉ R) ) ∧ (x ∈ A) ∧ (x ∉ P)
# тождественно ложна, то есть принимает значение 0 при любом значении переменной х?

p1, p2, q1, q2, r1, r2 = 10, 25, 15, 30, 25, 40

P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
R = [i / 10 for i in range(r1 * 10, r2 * 10 + 1)]

def f(x, A):
    return ((x in Q) <= (x not in R)) and (x in A) and (x not in P)

A = set([i / 10 for i in range(9 * 10, 41 * 10)])

for x in [i / 10 for i in range(9 * 10, 41 * 10)]:
    if f(x, A):
        A.remove(x)

print(sorted(A))

# [10; 30]
# Ответ: 30 - 10 = 20