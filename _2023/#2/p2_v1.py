# Логическая функция F задаётся выражением (¬x → y) ∧ (¬y ≡ z) ∧ w. На рисунке приведён частично заполненный
# фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки. Определите, какому столбцу таблицы
# истинности функции F соответствует каждая из переменных x, y, z, w.
#
# ? ? ? ? F
# 0   0   1
# 0       1
#   0     1
#
# В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы. Буквы в ответе
# пишите подряд, никаких разделителей между буквами ставить не нужно.
#
# Ответ: z y x w
from itertools import product, permutations

def f(x, y, z, w):
    return ((not x) <= y) and ((not y) == z) and w

for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat=8):
    t = (
        (0, x1, 0, x2, 1),
        (0, x3, x4, x5, 1),
        (x6, 0, x7, x8, 1),
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)

