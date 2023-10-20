# Логическая функция F задаётся выражением ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x)).
#
# ? ? ? ? F
# 1 0 1 1 1
# 1 0   0 1
# 1 0   0 1
#
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий
# неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F соответствует
# каждая из переменных x, y, z, w.
#
# Ответ: y z w x

from itertools import permutations, product

def f(x, y, z, w):
    return ((x and w) or (w and z)) == ((z <= y) and (y <= x))

for x1, x2 in product([0, 1], repeat=2):
    t = (
        (1, 0, 1,  1, 1),
        (1, 0, x1, 0, 1),
        (1, 0, x2, 0, 1)
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
