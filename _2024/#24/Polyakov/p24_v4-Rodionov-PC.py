"""
Текстовый файл 24-212.txt содержит строку из набора A, B, C, D, O, всего не более чем из 10^6 символов.
Определите максимальное количество идущих подряд пар символов вида «гласная + согласная».

Ответ: 202
"""

with open('Files/24-212.txt') as f:
    # Заменим все гласные на А, а все согласные на В.
    # Затем заменим все сочетания «гласная + согласная» на звездочку.
    s = f.readline().strip().replace('O', 'A').replace('C', 'B').replace('D', 'B').replace('AB', '*')
    # Оставшиеся буквы заменим на пробелы
    s = s.replace('A', ' ').replace('B', ' ')
    # Сплитуем строку и ищем самую длинную подстроку из звездочек
    print(max(map(len, s.split())))
