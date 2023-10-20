# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# При скольких целых неотрицательных значениях A формула
# ДЕЛ(А, 25) ∧ (ДЕЛ(х, 24) ∧ ДЕЛ(х, 75) → ДЕЛ(х, А))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
#
# Ответ: 8

def d(n, m):
    return n % m == 0


def f(aa, xx):
    return d(aa, 25) and ((d(xx, 24) and d(xx, 75)) <= d(xx, aa))

res = []

for A in range(1, 1000):
    for x in range(1, 1000):
        if f(A, x) == 0:
            break
    else:
        res.append(A)

print(len(res))
