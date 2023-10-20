# Текстовый файл 24-s1.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского
# алфавита (ABC…Z). Текст разбит на строки различной длины. Необходимо найти строку, содержащую наибольшее
# количество букв Q (если таких строк несколько, надо взять ту, которая в файле встретилась позже). Определите,
# какая буква встречается в этой строке реже всего (но присутствует!). Если таких букв несколько, надо взять ту,
# которая стоит раньше в алфавите. Запишите в ответе эту букву, а затем – сколько раз она встречается во всем файле.
#
# Пример. Исходный файл:
# ZZQAQB
# QAVQAB
# BAQTUB
# В этом примере в первой и второй строках по две букву Q, в третьей – одна. Берём вторую строку, т.к. она стоит в
# файле позже. В этой строке реже других встречаются буквы V и B (по одному разу), выбираем букву B, т. к. она
# раньше стоит в алфавите. В ответе для этого примера надо записать B4, так как во всех строках файла буква B
# встречается 4 раза.

from collections import Counter

with open('24-s1.txt') as f:
    lines = f.readlines()
    qi = -1
    maxq = 0
    lcount = len(lines)

    for i in range(lcount):
        lines[i] = lines[i].strip()
        qc = lines[i].count('Q')
        if qc > maxq:
            maxq = qc
            qi = i

    # Поиск самой часто-встречающейся буквы
    s = lines[qi]
    # Способ 1
    dic = {}  # Словарь, в котором ключ - это буква, а значение - это количество в строке

    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

    # Для каждого элемента при сравнении в функции min будет вызвана функция из key.
    # То есть для каждого ключа в словаре dic будет вызвана функция dic.get(), а ключ будет аргументом функции.
    # Таким образом будет найден минимум среди значений, а не ключей.
    char1 = min(dic, key=dic.get)

    # Способ 2
    x = Counter(s).most_common()
    char2 = x[len(x) - 1][0]

    # Результат
    print(char1, sum(s.count(char1) for s in lines))
    print(char2, sum(s.count(char2) for s in lines))

# Ответ: C38412