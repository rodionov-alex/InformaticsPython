# Логическая функция F задаётся выражением ((x → z) → y) ∨ ¬w. На рисунке приведён частично заполненный
# фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки. Определите, какому столбцу
# таблицы истинности функции F соответствует каждая из переменных x, y, z, w.
#
# ? ? ? ? F
# 1 0     0
#   1 0   0
# 0       0
#
# В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы. Буквы в
# ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
#
# Ответ: z x y w

from itertools import product, permutations


def f(x, y, z, w):
    return ((x <= z) <= y) or (not w)

tb = (
        (1, 0, '*', '*', 0),
        ('*', 1, 0, '*', 0),
        (0, '*', '*', '*', 0)
    )

for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (1, 0, x1, x2, 0),
        (x3, 1, 0, x4, 0),
        (0, x5, x6, x7, 0)
    )

    for p in permutations('xyzw', r=4):
        if all(f(**dict(zip(p, m))) == m[-1] for m in t):
            print(*p)
