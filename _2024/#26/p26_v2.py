"""
Проводится вычислительный эксперимент для определения необходимого количества самокатов на разных парковках
города в начальный момент времени. Всего есть M парковок с номерами от 1 до М. Поступило всего N заявок на
аренду самокатов. В каждой заявке указано время начала аренды в минутах от начала суток, продолжительность
аренды, а также номера парковок старта и финиша. Будем считать, что заряда самоката хватает на весь день и
самокат может быть арендован со следующей минуты после окончания предыдущей аренды. Определите, начиная с
какого момента (в минутах от начала эксперимента) было арендовано максимальное количество самокатов, и номер
парковки, на которой нужно установить максимальное количество самокатов.
Входные данные представлены в файле 26-123.txt следующим образом. Первая строка входного файла содержит два
натуральных числа, записанных через пробел: M (1 ≤ M ≤ 100) – количество парковок, и N (1 ≤ N ≤ 106) –
количество заявок. Каждая из N последующих строк описывает содержит четыре целых числа: время начала аренды
в минутах от начала суток, длительность аренды в минутах, номер парковки старта и номер парковки финиша.
В ответе запишите два числа: сначала время (в минутах от начала эксперимента), когда впервые началась аренда
максимального количества самокатов, затем – номер парковки, на которой нужно установить максимальное количество
самокатов.
Пример входного файла:
2 3
1 4 2 2
3 6 1 1
5 9 1 2
При таких исходных данных нужно три самоката: два в начале размещаются на парковке 1 и один – на парковке 2.
Одновременно в аренде находятся максимум два самоката (с 3-й по 8-ю минуту включительно). Ответ: 3 1.

Ответ: 400 13
"""

with open('Files/26-123.txt') as f:
    m, n = tuple(map(int, f.readline().split()))
    # Заявки на аренду самоктов
    data = sorted([tuple(map(int, x.split())) for x in f], key=lambda x: x[0])
    # Парковки
    parkings = dict.fromkeys(range(1, m + 1), 0)
    # Таймлайн
    timeline = [0] * 1440

    for begin, duration, p_start, p_finish in data:
        # Заполнить таймлайн
        for i in range(begin, begin + duration):
            try:
                timeline[i] += 1
            except IndexError:
                # print(d)  # самокат арендован в конце суток, и вернется на следующие
                pass

        # Заполнить данные о парковках: откуда убыл - отнять единицу, куда прибыл - прибавить.
        parkings[p_start] -= 1
        parkings[p_finish] += 1

    # Ответ: 1) индекс минуты с максимальным количеством заявок на самокат
    #        2) номер парковки с минимальным значением (отрицательным - это количество необходимых самокатов)
    print(timeline.index(max(timeline)), min(parkings, key=parkings.get))
