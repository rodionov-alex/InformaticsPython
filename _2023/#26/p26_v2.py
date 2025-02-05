# Управляющей компании поступили жалобы об отсутствии капитального ремонта. В каждой жалобе указан номер дома
# и номер подъезда, где необходим ремонт. Компания решила в первую очередь сделать ремонт в тех домах, в которых
# есть подъезд без жалоб (чтобы расположить в нём строительные материалы) и не менее чем в 3 соседних подъездах
# жалобы присутствуют.
# Найдите общее количество жилых домов, которые планируется отремонтировать, и минимальный номер подъезда для
# размещения материалов, который находится в доме с максимальным номером.
# Входные данные представлены в файле 26-95.txt следующим образом. В первой строке входного файла записано
# натуральное число N, не превышающее 100000 – количество подъездов с жалобами. Каждая из следующих N строк
# содержит два натуральных числа: номер дома (не превышает 2000) и номер подъезда в доме (не превышает 5000).
# Запишите в ответе два числа: количество домов, где есть такие подходящие подъезды, и минимальный номер
# подъезда в подходящем доме с максимальным номером.
# Пример входного файла::
# 8
# 1 5
# 1 6
# 1 7
# 1 9
# 2 1
# 2 12
# 1 10
# 2 24
# При таких исходных данных есть два подходящих подъезда в 1-ом доме: № 4 (3 соседних подъезда с жалобами: 5, 6 и 7)
# и № 8 (4 соседних подъезда с жалобами: 6, 7, 9 и 10). Ответ: 1 4.
#
# Ответ: 14 3036

with open('26-95.txt') as f:
    data = [tuple(int(y) for y in x.split()) for x in f.readlines()[1:]]
    houses_dic = {}  # словарь домов, дом - ключ, подъезды - значения

    # Наполнение словаря
    for d in data:
        if d[0] in houses_dic.keys():
            houses_dic[d[0]].append(d[1])
        else:
            houses_dic[d[0]] = [d[1]]

    hoгses_to_repair = 0  # количество подходящих для ремонта домов
    max_house = 0
    max_diffs = []

    for k in sorted(houses_dic.keys()):
        # В доме должно быть не менее 3 подъездов
        if len(houses_dic[k]) >= 3:
            # Сортированный список подъездов
            porches = sorted(houses_dic[k])
            # Массив разниц между номерами подъездов
            diffs = []
            # Заполнение массива
            for i in range(len(porches) - 1):
                diffs.append(porches[i + 1] - porches[i])
            # Перебор разниц для определения подходит ли дом
            for i in range(len(diffs) - 1):
                sr = diffs[i:i + 2]  # Срез двух разниц
                # Нужны либо 3 подъезда рядом, то есть с разницами жду номерами [1, 1]
                # Нужны либо 2 подъезда рядом и один через один, то есть с разницами жду номерами [1, 2] или [2, 1]
                if sr == [1, 1] or sr == [1, 2] or sr == [2, 1]:
                    hoгses_to_repair += 1       # Увеличиваем счетчик домов
                    max_house = k               # Запоминаем номер последнего подходящего дома, он и будет максимальным
                    max_diffs = diffs.copy()    # Запоминаем разницы номеров подъездов этого дома
                    break

    porches = sorted(houses_dic[max_house])  # Подъезды дома с максимальным номером
    porch = 0                                # Минимальный номер подъезда для размещения материалов

    for i in range(len(max_diffs) - 1):
        sr = max_diffs[i:i + 2]  # Срез двух разниц

        # 3 подъезда в ряд - берем подъезд перед тройкой, либо после нее, если твойка подъездов в начале дома
        if sr == [1, 1]:
            porch = porches[i] - 1 if porches[i] - 1 > 0 else porches[i + 2] + 1
            break
        # 2 подъезда рядом и один через один - берем тот что после пары
        elif sr == [1, 2]:
            porch = porches[i + 1] + 1
            break
        # один подъезд и через один 2 подъезда рядом - берем тот что перед парой
        elif sr == [2, 1]:
            porch = porches[i] + 1
            break

    # Вывод результата
    print(hoгses_to_repair, porch)
