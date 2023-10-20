# Сколько существует целых значений числа A, при которых формула
# ((x < 6) → (x^2 < A)) ∧ ((y^2 ≤ A) → (y ≤ 6))
# тождественно истинна при любых целых неотрицательных x и y?

def f(x, y, A):
    return ((x < 6) <= (x * x < A)) and ((y * y <= A) <= (y <= 6))

res = []

for A in range(100):
    for x in range(100):
        good = True

        for y in range(100):
            if f(x, y, A) == 0:
                good = False
                break

        if not good:
            break

    if good:
        res.append(A)


print(len(res))