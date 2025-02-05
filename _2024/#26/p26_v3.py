"""
В отделении банка используется система распознавания лиц, с помощью которой фиксируется время, когда посетитель
пришел в отделение и время, когда он вышел. Для удобства время хранится как целое число, показывающее, сколько
секунд прошло от начала суток до события. Посетителей банка обслуживают операторы, которые пронумерованы, начиная
с 1. Посетитель обслуживается свободным оператором с минимальным номером. Оператор может принять следующего
посетителя в ту же секунду, как обслуживаемый им посетитель покидает здание. На обслуживание требуется, как минимум,
одна секунда. Если свободных операторов нет, посетитель становится в очередь. Посетитель может не дождаться своей
очереди и уйти.
Определите, сколько посетителей было обслужено операторами и номер оператора, обслужившего последнего посетителя.
Входные данные представлены в файле 26-132.txt следующим образом. Первая строка входного файла содержит натуральное
число N (1 ≤ N ≤ 10000) – количество посетителей, и натуральное число K (1 ≤ K ≤ 1000) – количество операторов в
отделении. В каждой из последующих N строк записаны через пробел в возрастающем порядке по два целых неотрицательных
числа: T1 (0 ≤ T1 ≤ 86399) – время, в которое посетитель зашел в отделение и T2 (T1 ≤ T2 ≤ 86399) – время, когда
он вышел. Считается, что до начала суток и после их окончания в помещении посетителей не было. Все, кто зашел в
отделение, успел выйти до закрытия.
Запишите в ответе два числа: количество посетителей, обслуженных операторами, и номер оператора, обслужившего
последнего посетителя.
Пример входного файла:
6 2
1 50
2 40
5 100
50 86000
60 70
70 100
При таких исходных данных были успешно обслужены 4 посетителя, пятый и шестой ушли раньше, чем подошла их очередь.
Последнего посетителя обслуживал оператор 1. Ответ: 4 1.

Ответ: 2108 9
"""

with open('Files/26-132.txt') as f:
    n, k = tuple(map(int, f.readline().split()))
    visitors = sorted([tuple(map(int, x.split())) for x in f])
    operators = [-1] * k    # Список опреаторов
    events_log = []         # Лог событий
    queue = []              # Очередь на прием
    last = 0                # Номер последнего оператора
    count = 0               # Количество принятых посетителей
    # Заполним лог событий
    for i in range(len(visitors)):
        arrive, leave = visitors[i]
        events_log.append((arrive, 1, i))  # 1 пришел
        events_log.append((leave, -1, i))  # -1 ушел
    # Сортировка лога по времени события
    events_log.sort()
    # Перебор событий
    for event in events_log:
        # Пришел посетитель
        if event[1] > 0:
            # Добавить в очередь
            queue.append(event)
        # Ушел посетитель
        else:
            try:
                # Освободить оператора, если посетитель был у него на приеме
                operators[operators.index(event[2])] = -1
            except ValueError:
                # Если у оператора не найден, то удалить из очереди
                for q in queue:
                    if q[2] == event[2]:
                        queue.remove(q)
                        break
                # Когда ушел из очереди оператор не освободился
                continue
        # Распределить посетителей из очереди по операторам
        for i in range(operators.count(-1)):
            if len(queue):
                count += 1
                last = operators.index(-1)
                operators[last] = queue.pop(0)[2]  # Опреатору записать номер посетителя
            else:
                break

    print(count, last + 1)
