"""
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды,
в обеих командах v и w обозначают цепочки символов.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет,
эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось(01) ИЛИ нашлось(02) ИЛИ нашлось(03)
  заменить(01, 2302)
  заменить(02, 10)
  заменить(03, 201)
КОНЕЦ ПОКА
КОНЕЦ
Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки. После
выполнения данной программы получилась строка, содержащая 51 единицу, 29 двоек и 23 тройки. Сколько троек
было в исходной строке?
"""

def f(x1, x2, x3):
    s = '0' + '3' * x3 + '1' * x1 + '2' * x2

    while '01' in s or '02' in s or '03' in s:
        if '01' in s:
            s = s.replace('01', '2302', 1)
        if '02' in s:
            s = s.replace('02', '10', 1)
        if '03' in s:
            s = s.replace('03', '201', 1)

    return s.count('1'), s.count('2'), s.count('3')

"""
print(f(1, 0, 0))
print(f(0, 1, 0))
print(f(0, 0, 1))

    1   2   3
1)  1   1   1
2)  1   0   0
3)  1   2   1
"""

max1 = 23
max2 = 51
max3 = 14

for x1 in range(max1 + 1):
    for x2 in range(max2 + 1):
        for x3 in range(max3 + 1):
            if f(x1, x2, x3) == (51, 29, 23):
                print(x3)
