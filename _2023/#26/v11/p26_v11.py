# В одном из конференц-залов города Н проводится научная конференция. Известно, какие места в зале уже забронированы
# для участников конференции из других городов и для участников конференции из города Н. Найдите ряд с наибольшим
# номером, в котором есть ровно сто свободных мест подряд между участниками из других городов, а также хотя бы пятьсот
# мест, занятых участниками из города Н. Гарантируется, что есть хотя бы один ряд, удовлетворяющий этому условию.
# Входные данные представлены в файле 26-85.txt следующим образом. В первой строке входного файла записано натуральное
# число N – общее количество занятых мест (1 ≤ N ≤ 600 000). В каждой из следующих N строках находятся по три
# натуральных числа, не превышающих 25 000. Первые два числа – это номер ряда и место в ряду, занятое участником
# конференции. Если третье число равно 0, то место занято участником из города Н, а если оно равно 1, то участником
# из другого города.
# Запишите в ответе два числа: максимальный номер подходящего ряда и количество мест, занятых в этом ряду участниками
# из других городов.
# Пример входного файла:
# 15
# 1 1 0
# 1 3 1
# 1 5 0
# 1 7 1
# 1 8 0
# 2 3 1
# 2 8 1
# 2 9 0
# 2 10 0
# 3 1 0
# 3 2 1
# 3 6 1
# 3 7 0
# 3 8 0
# 3 9 0
# В примере требуется найти ряд, в котором есть ровно три свободных места между участниками из других городов, а
# также хотя бы четыре занятых места, занятые участниками из города Н. В 3-м ряду есть 3 свободных места подряд
# между участниками из других городов (места 3, 4 и 5) и 4 места заняты участниками из города Н. В этом ряду 2
# места заняты участниками из других городов (места 2 и 6). Ответ: 3 2.
#
# Ответ: 17384 5090

with open('26-85.txt') as f:
    data = sorted([tuple(int(y) for y in x.split()) for x in f.readlines()[1:]])  # Данные СОРТИРОВАНЫ
    tickets_D = {}
    tickets_H = {}

    for d in data:
        row, place, town = d

        if town == 0:
            if row in tickets_H:
                tickets_H[row].append(place)
            else:
                tickets_H[row] = [place]
        else:
            if row in tickets_D:
                tickets_D[row].append(place)
            else:
                tickets_D[row] = [place]

    mx_row = -1

    for row in tickets_H:
        if row in tickets_D and len(tickets_D[row]) >= 2 and len(tickets_H[row]) >= 500:
            for i in range(1, len(tickets_D[row])):
                # Разница должна быть равна 101 потому, что считаются места между
                if tickets_D[row][i] - tickets_D[row][i - 1] == 101:
                    t_count = len(tickets_H[row])  # Количество занятных мест из города Н
                    p = 0

                    # Проверка занятых мест города Н
                    while tickets_H[row][p] <= tickets_D[row][i] and p < t_count:
                        # Проверка, что занятое место не находится в свободной сотне
                        if tickets_D[row][i - 1] <= tickets_H[row][p] <= tickets_D[row][i]:
                            break

                        p += 1
                    # Проверка пройдена
                    else:
                        mx_row = row

    print(mx_row, len(tickets_D[mx_row]))
