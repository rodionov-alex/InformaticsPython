# Семья М. собирается купить билеты на самолет, чтобы полететь на отдых. Они выбрали рейс с двухэтажным самолётом.
# В семье, помимо папы и мамы, имеется двое детей, и билеты нужно купить так, чтобы вся семья летела в одном ряду
# на соседних местах. Дети хотят смотреть в окно, поэтому нужно одно место у окна. Места у окон считаются самые
# крайние места в каждом ряду (первое и последнее).
# Известно, какие места уже куплены (заняты). Найдите ряд с наибольшим номером, в котором можно забронировать четыре
# подряд идущие свободные места с одним местом у окна. Гарантируется, что есть хотя бы один ряд, удовлетворяющий этому
# условию. Ряды, информации о которых нет в списке бронирования, не учитываются.
# Входные данные представлены в файле 26-94.txt следующим образом. В первой строке входного файла находится два числа:
# N – количество занятых мест (натуральное число, не превышающее 20 000) и K – количество мест в каждом ряду самолета
# (натуральное число, не превышающее 10). Каждая из следующих N строк содержит три натуральных числа, не превышающих
# 100 000: номер этажа, номер ряда и номер занятого места в этом ряду.
# Запишите в ответе два числа: максимальный номер подходящего ряда и общее количество таких рядов, в которых можно
# забронировать четыре подряд идущие свободных места с одним местом у окна.
# Пример входного файла::
# 5 6
# 1 50 2
# 2 23 1
# 1 50 3
# 2 30 5
# 1 1 6
# При таких исходных данных есть два подходящих ряда: 1-й ряд на 1-м этаже и 23-й ряд на 2-м этаже. Ответ: 23 2.
#
# Ответ: 9996 5029

with open('26-94.txt') as f:
    places_in_row = int(f.readline().split()[1])
    need_places = 4
    data = [tuple(map(int, x.split())) for x in f.readlines()]
    plane_1 = {}  # 1 этаж
    plane_2 = {}  # 2 этаж
    max_row = 0
    good_rows = 0

    # Перебор данных и заполнение словарей, где ключ это номер ряда, а ряд это список длиной places_in_row.
    # Ряд состоит из 0 и 1, где 0 - это свободное место, а 1 - занятое.
    for d in data:
        floor, row, place = d

        if floor == 1:
            if row not in plane_1.keys():
                plane_1[row] = [0] * places_in_row

            plane_1[row][place - 1] = 1
        else:
            if row not in plane_2.keys():
                plane_2[row] = [0] * places_in_row

            plane_2[row][place - 1] = 1

    # Проверка 1 этажа
    for r in plane_1.keys():
        row = plane_1[r]

        # Так как нужны места у окна, то суммируем крайние места
        if sum(row[:need_places]) == 0 or sum(row[-need_places:]) == 0:
            good_rows += 1
            max_row = max(max_row, r)

    # Проверка 2 этажа
    for r in plane_2.keys():
        row = plane_2[r]

        # Так как нужны места у окна, то суммируем крайние места
        if sum(row[:need_places]) == 0 or sum(row[-need_places:]) == 0:
            good_rows += 1
            max_row = max(max_row, r)

    print(max_row, good_rows)
