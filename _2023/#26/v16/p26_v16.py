# В лесополосе высаживают плодовые деревья рядами на одинаковом расстоянии друг от друга. Между соседними саженцами
# в одном ряду расстояние 10 метров. В каждом ряду высаживают разные виды плодовых деревьев. Через какое-то время
# с помощью аэросъемки определяют, какие саженцы прижились, а какие – нет. Для успешного перекрестного опыления
# необходимо, чтобы дерево было на расстоянии не более 20 метров от прижившегося дерева того же вида, иначе оно
# не будет плодоносить. Определите, какое минимальное количество деревьев нужно посадить, чтобы все деревья могли
# плодоносить, и номер ряда, в котором необходимо дополнительно посадить максимальное количество деревьев.
# Входные данные представлены в файле 26-80.txt следующим образом. В первой строке находится число N - количество
# занятых мест (натуральное число, не превышающее 10 000). Каждая из следующих N строк содержит два натуральных числа,
# не превышающих 100 000: номер ряда и номер занятого места.
# Запишите в ответе два числа: минимальное количество деревьев, которые нужно посадить в лесополосе, и номер ряда,
# где нужно посадить максимальное количество деревьев (если таких рядов несколько, нужно вывести номер первого из них).
# Пример входного файла:
# 7
# 1 3
# 1 5
# 1 8
# 2 2
# 2 5
# 3 1
# 3 9
# В этом случае достаточно посадить 4 дерева в позициях (1, 7), (2, 4), (3, 3) и (3, 7). Наибольшее количество
# деревьев (2) нужно посадить в 3-м ряду. Ответ: 4 3.
#
# Ответ: 9990 4902

with open('26-80.txt') as f:
    data = sorted([tuple(int(y) for y in x.split()) for x in f.readlines()[1:] if ' ' in x])
    rows_dic = {}

    # Заполнение словаря грядок
    for d in data:
        if d[0] in rows_dic.keys():
            rows_dic[d[0]].append(d[1])
        else:
            rows_dic[d[0]] = [d[1]]

    need_to_plant = 0   # Общее количество саженцев для посадки
    mx_row = -1         # Ряд с максимальным количеством саженцев для посадки
    mx_plant = 0        # Максимальное количество саженцев для посадки в ряду

    for k in rows_dic.keys():
        row = rows_dic[k]       # Ряд с номерами мест посаженных деревьев
        plant = 0               # Количество саженцев, необходимых для посадки в ряду
        pCount = len(row)       # Количество посаженных деревьев
        lastIndex = pCount - 1  # Индекс последнего дерва

        # Если в ряду всего одно дерево, то ему нужен только 1 саженец
        if pCount == 1:
            plant = 1
        # Если больше 1 дерева:
        else:
            neighbour = -3  # место для подсадки саженца

            # Перебор посаженных деревьев
            for i in range(pCount - 1):
                # Если расстояние до подсаженного саженца и соседнего дерева слишком велико
                if row[i] - neighbour > 2 and row[i + 1] - row[i] > 2:
                    # то необходимо подсадить саженец справа
                    plant += 1
                    neighbour = row[i] + 2
                    # print((k, neighbour))
            # Проверка последнего дерева в ряду, если оно далеко от соседа или подсаженного саженца
            if row[pCount - 1] - neighbour > 2:
                # то к нему необходимо подсадить саженец слева
                plant += 1
                # print((k, row[pCount - 1] - 2))

        # Добавить количество саженцев, необходимых для посадки в ряду, к общему количеству
        need_to_plant += plant

        # Сравнение с максимальным количеством
        if plant > mx_plant:
            mx_plant = plant
            mx_row = k

    print(need_to_plant, mx_row)