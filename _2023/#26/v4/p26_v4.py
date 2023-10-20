# При проведении эксперимента заряженные частицы попадают на чувствительный экран, представляющий из себя матрицу
# пикселей размером 10000 на 10000 точек. При попадании очередной частицы на экран в файл записываются координаты
# чувствительного элемента: номер строки (целое число от 1 до 10000) и номер позиции в строке (целое число от 1 до
# 10000) и её заряд (+/-). Положительно заряженная частица включает пиксель, а отрицательно заряженная выключает.
# Положительная частица не влияет на включенный пиксель, как и отрицательно заряженная на выключенный. Определите
# на момент завершения эксперимента номер строки, в которой находится наибольшая непрерывная цепочка включенных
# пикселей.
# Входные данные представлены в файле 26-92.txt следующим образом. В первой строке записано количество строк с
# данными N (1 ≤ N ≤ 1000000). В каждой из следующих N строк записаны два натуральных числа, не превышающих 10000
# – координаты сработавшего чувствительного элемента (сначала строка, затем позиция пикселя в этой строке), а
# затем – знак «+» или «–», отделенный от чисел пробелом.
# Запишите в ответе два числа: сначала длину наибольшей непрерывной цепочки включенных пикселей одной строки,
# затем – номер строки, в которой находятся эта цепочка. Если таких строк несколько, укажите номер последней
# из подходящих строк.
# Пример входного файла:
# 8
# 2 5 +
# 2 6 +
# 1 2 +
# 2 7 +
# 1 3 -
# 2 6 +
# 2 4 +
# 2 7 -
# При таких исходных данных задачи на момент завершения эксперимента в строке 1 включен только пиксель в позиции 2,
# а в строке 2 – три пикселя подряд в позициях 4, 5 и 6. Самая Ответ: 2 3.
#
# Ответ: 7 3860

# !!! Заранее заменил в файле 26-92.txt все '+' на 1 и все '-' на 0 !!!
with open('26-92.txt') as f:
    data = [tuple(map(int, x.split())) for x in f.readlines()[1:]]
    screen = {}

    for d in data:
        x, y, sign = d

        # Если координата х уже зарегистрирована
        if x in screen:
            row = screen[x]  # строка

            # Если у уже есть в строке, но его надо выключить
            if y in row and sign == 0:
                # то удаляем его из строки
                row.remove(y)
            # Если у в строке нету и его надо включить
            elif y not in row and sign == 1:
                # то добавляем его в строку
                row.append(y)
        # Если строки с координатой х еще нет и ее надо включить
        elif sign == 1:
            # то добавляем ее с единственной координатой у
            screen[x] = [y]

    max_pixels_in_a_row = 0
    that_row = 0

    # Перебор всех строк экрана
    for x in screen:
        row = sorted(screen[x])
        cur_max_len = 1
        cur_len = 1

        for i in range(1, len(row)):
            # Если разница с предыдущей координатой равна 1, то пиксели находятся рядом
            if row[i] - row[i - 1] == 1:
                cur_len += 1  # Увеличить длину текущей цепочки пикселей
            else:
                # Сравнить с максимальной йепочкой в данной строке и сбросить текущую длину
                cur_max_len = max(cur_max_len, cur_len)
                cur_len = 1

        # Сравнение максимальной длины цепочки на всем экране
        if cur_max_len >= max_pixels_in_a_row:
            max_pixels_in_a_row = cur_max_len
            that_row = x

    print(max_pixels_in_a_row, that_row)
