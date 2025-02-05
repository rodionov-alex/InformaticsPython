# На числовой прямой даны два отрезка: P = [117; 158] и Q = [129; 180]. Найдите наименьшую возможную длину
# отрезка A, при котором формула
#
# (x ∈ P) → ( ((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P)) )
#
# тождественно истинна, то есть принимает значение 1 при любых x.
#
# Ответ: 29

p1, p2, q1, q2 = 117, 158, 129, 180

P = [x / 10 for x in range(p1 * 10, p2 * 10 + 1)]
Q = [x / 10 for x in range(q1 * 10, q2 * 10 + 1)]
A = set()

def f(x):
    return (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))

for x in [i / 10 for i in range(p1 * 10 - 1, q2 * 10 + 1)]:
    if not f(x):
        A.add(x)

print(sorted(A))

# Ответ: [129; 158]  158 - 129 = 29
# Ответ: 29
