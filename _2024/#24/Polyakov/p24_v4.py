"""
Текстовый файл 24-212.txt содержит строку из набора A, B, C, D, O, всего не более чем из 10^6 символов.
Определите максимальное количество идущих подряд пар символов вида «гласная + согласная.

Ответ: 202
"""

with open('Files/24-212.txt') as f:
    s = f.readline().strip()
    # Заменить гласные на 1, а согласные на 0
    s = s.replace('O', 'A').replace('C', 'B').replace('D', 'B')
    # Разделить стоящие рядом A пробелом
    while 'AA' in s:
        s = s.replace('AA', 'A A')
    # Разделить стоящие рядом B пробелом
    while 'BB' in s:
        s = s.replace('BB', 'B B')

    print(max(list(map(len, s.split()))) // 2)  # делим на 2 т.к. ищем пары «гласная + согласная
