# Два грузовика собирают мусор на кольцевой автодороге. Известно, что грузовики заезжают на кольцевую автодорогу
# и съезжают с неё в одном из пунктов приема мусора. Грузовики движутся по дороге в противоположных направлениях,
# собирая мусор во всех пунктах приема мусора, через которые построен их маршрут. Мусор, находящийся в пунктах, где
# грузовики заезжают и съезжают с кольца, полностью забирает одна из машин. Пункты приема мусора располагаются на
# расстоянии 1 км друг от друга.
# Грузовики имеют одинаковую грузоподъемность. Найдите минимальную необходимую грузоподъемность грузовиков, при
# которой они могут собрать весь мусор на кольцевой автодороге. Для этого варианта определите минимальное из
# расстояний, которые проедут по кольцевой дороге грузовики с найденной грузоподъемностью.
# Входные данные. Даны два входных файла (файл A и файл B), каждый из которых в первой строке содержит число
# N (1 ≤ N ≤ 10 000 000) – количество пунктов сбора мусора на кольцевой автодороге. В каждой из следующих N строк
# находится натуральное число, не превышающее 1000 – количество мусора в контейнере. Числа указаны в порядке
# расположения контейнеров на автомагистрали, начиная с первого километра.
# Пример входного файла:
# 6
# 8
# 20
# 5
# 13
# 7
# 19
# При таких исходных данных один грузовик может собрать мусор в пунктах со 2 по 4 (20+5+13 = 38), второй в
# пунктах 1, 6, 5 (8+19+7 = 34).
# В этом случае минимальная грузоподъемность составит 38 единиц, а длина маршрута – 2 км: от п. 2 до п. 4
# (грузовик заезжает в п. 2 и съезжает с трассы в п. 4) или от п. 1 до п. 5. Ответ: 2.
# В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
#
# Ответ:
from math import ceil
from tqdm import tqdm

with open('27-125b.txt') as f:
    points_count = int(f.readline())
    data = [int(x) for x in f]
    # points_count = 6
    # data = [8, 20, 5, 13, 7, 19]

    # Рассчет грузоподъемности
    points_per_truck = ceil(points_count // 2)
    truck_1 = data[:points_per_truck]
    truck_2 = data[points_per_truck:]
    weight_1 = sum(truck_1)
    weight_2 = sum(truck_2)
    min_weight = max(weight_1, weight_2)

    # print(0, truck_1, weight_1)
    # print(0, truck_2, weight_2)

    for i in tqdm(range(points_per_truck)):
        trash_1 = truck_1.pop(0)
        trash_2 = truck_2.pop(0)
        truck_1.append(trash_2)
        truck_2.append(trash_1)
        weight_1 = weight_1 - trash_1 + trash_2
        weight_2 = weight_2 - trash_2 + trash_1

        mx = max(weight_1, weight_2)

        if min_weight > mx:
            min_weight = mx

        # print(i + 1, weight_1)
        # print(i + 1, weight_2)

    # Расчет кратчайшего расстояния
    min_weight = 6026360
    cur_weight = data[0]
    min_length = float('inf')
    truck = [data[0]]

    for i in tqdm(range(1, points_count)):
        trash = data[i]
        truck.append(trash)
        cur_weight += trash

        if cur_weight > min_weight:
            while cur_weight > min_weight:
                cur_weight -= truck.pop(0)

            min_length = min(min_length, len(truck))

    print(min_weight, min_length)








