# На отрезке [100 000; 500 000] найдите такие числа, у которых больше 3 различных простых делителей,
# причем все они образуют арифметическую прогрессию с разностью отличной от нуля. В качестве ответа
# запишите найденные числа в порядке возрастания, справа от каждого числа запишите произведение
# количества простых делителей на разность их арифметической прогрессии.
#
# Ответ: 101065 48
#        107525 24
#        124729 24
#        177289 48
#        236555 24
#        278185 72
#        365585 24
#        494615 24

# Простое число
def is_simple(k):
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    for m in range(3, int(k ** 0.5) + 1, 2):
        if k % m == 0:
            return False

    return True

# Простые делители
def simple_divs(num):
    simp_divs = []

    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            if is_simple(d):
                simp_divs.append(d)

                d2 = num // d

                if d2 != d and is_simple(d2):
                    simp_divs.append(d2)

    return simp_divs


for n in range(100000, 500001):
    # Поиск простых делителей
    divs = simple_divs(n)

    if len(divs) > 3:
        prog = []
        # Прогрессия, разность между соседними делителями
        for i in range(len(divs) - 1):
            prog.append(divs[i + 1] - divs[i])
        # Разность в арифметической прогрессии должна быть одна
        if len(set(prog)) == 1:
            print(n, len(divs) * prog[0])

