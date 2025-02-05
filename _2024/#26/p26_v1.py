"""
Начальник ведет прием граждан. При этом, при формировании очередности приема приняты следующие правила:
    1) пенсионеры пользуются преимуществом перед всеми остальными гражданами;
    2) женщины пользуются преимуществом перед мужчинами;
    3) посетители одной категории принимаются в порядке «живой» очереди. Каждый приём длится определенное время (мин.).
Определите, сколько посетителей принято к заданному моменту времени и сколько из них относятся к той же категории,
что и посетитель, находящийся на приеме в данный момент времени.
Входные данные представлены в файле 26-134.txt следующим образом. Первая строка входного файла содержит два
натуральных числа N и T (1 ≤ N ≤ 1000, 1 ≤ T ≤ 10000) – количество принятых людей и интересующий нас момент
времени, соответственно. Каждая из следующих N строк содержит три значения: время, когда посетитель пришел
на прием; длительность приема; категория посетителя, одна из трех букв: W (женщина), M (мужчина) и G (пенсионер).
Запишите в ответе два числа: количество посетителей, принятых к моменту времени T (считая посетителя,
находящегося на приёме в этот момент), и количество принятых посетителей той же категории, что и человек,
находящийся на приеме в момент времени T.
Пример входного файла:
5 12
1 6 W
4 7 M
5 3 G
8 9 M
11 5 G
При таких исходных данных с 1-й по 7-ю минуту на приёме будет находиться женщина, пришедшая в 1-ю минуту.
С 7-й по 10-ю минуту пенсионер, пришедший в 5-ю минуту. С 10-й по 17-ю – мужчина, пришедший в 4-ю минуту.
Всего будет принято 3 человека, из них один мужчина, находящийся на приёме в момент 12. Ответ: 3 1.

Ответ: 80 77
"""

# Приоритет приема граждан:
# G (пенсионер) = 0, W (женщина) = 1, M (мужчина) = 2.
def priority(s):
    if s == 'G':
        return 0
    if s == 'W':
        return 1
    return 2

# Преобразование строки в кортеж.
# Данные гражданина: время приема, длительность приема, категория гражданина.
def get_data(sdata):
    sdata = sdata.split()
    return int(sdata[0]), int(sdata[1]), sdata[2]

with open('Files/26-134.txt') as f:
    n, t = tuple(map(int, f.readline().split()))
    # Сортированный по времени список посетителей
    visitors = sorted([get_data(x) for x in f])
    # Количество принятых граждан по категориям
    recepted_visitors = dict.fromkeys('GWM', 0)
    # Таймлайн приема граждан
    timeline = [0] * 1440
    # Очередь на прием
    visitors_queue = []

    for i in range(t + 1):
        changed = False
        # Добавление посетителей в очередь
        while len(visitors) and visitors[0][0] == i:
            visitors_queue.append(visitors.pop(0))
            changed = True

        # Сортировка сначала по категории, потом по времени прихода
        if changed:
            visitors_queue.sort(key=lambda x: (priority(x[2]), x[0]))

        # Если время приема свободно, то принять гражданина очереди
        if timeline[i] == 0 and len(visitors_queue) > 0:
            visitor = visitors_queue.pop(0)
            # Заполнить время приема на таймлайне типом принятого гражданина
            for j in range(i, i + visitor[1]):
                timeline[j] = visitor[2]
            # Добавить гражданина в принятые согласно его категории
            recepted_visitors[visitor[2]] += 1

    print(timeline)
    # Ответ
    print(sum(recepted_visitors.values()), recepted_visitors[timeline[t]])
