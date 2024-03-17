"""
Входной файл содержит сведения о заявках на проведение занятий в конференц-зале. В каждой заявке указаны время
начала и время окончания мероприятия (в минутах от начала суток). Если время начала одного мероприятия меньше
времени окончания другого, то провести можно только одно из них. Если время окончания одного мероприятия совпадает
с временем начала другого, то провести можно оба. Определите максимальное количество мероприятий, которое можно
провести в конференц-зале и самое позднее время окончания последнего мероприятия.
Входные данные представлены в файле 26-128.txt следующим образом. Первая строка входного файла содержит натуральное
число N (1 ≤ N ≤ 1000) – количество заявок на проведение мероприятий. Следующие N строк содержат пары чисел,
обозначающих время начала и время окончания мероприятий. Каждое из чисел натуральное, не превосходящее 1440.
Запишите в ответе два числа: максимальное количество мероприятий, которое можно провести в конференц-зале и самое
позднее время окончания последнего мероприятия (в минутах от начала суток).
Пример входного файла:
5
10 150
100 110
131 170
131 180
120 130
При таких исходных данных можно провести максимум три мероприятия, например, по заявкам 2, 3 и 5.
Конференц-зал освободится самое позднее на 180-й минуте, если состоятся мероприятия по заявкам 2, 4, 5. Ответ: 3 180.

Ответ: 16 1345
"""

with open('Files/26-128.txt') as f:
    n = int(f.readline())
    # Список мероприятий отсортированный по возрастанию времени окончания
    events = sorted([tuple(map(int, x.split())) for x in f], key=lambda x: x[1])
    # Мероприятия, запланированные для проведения. Сразу возьмем мероприятие которое раньше всех закончится.
    planned_events = [events[0]]
    # Планировка мероприятий
    for i in range(1, len(events)):
        # Добавить очередное мероприятие если его началу не мешает последнее мероприятие в плане
        if events[i][0] >= planned_events[-1][1]:
            planned_events.append(events[i])
    # Уберем последнее мероприятие из плана для поиска такого, которое бы заканчивалось позже всех
    planned_events.pop()
    # Отсортируем мероприятия по убыванию так, чтобы в начале списка events оказались мероприятия
    # с самым поздним окончанием и самым поздним стартом.
    for event in sorted(events, reverse=True, key=lambda x: (x[1], x[0])):
        # Ищем первое мероприяте, начало которого позже окончания последнего мероприятия в плане
        if event[0] >= planned_events[-1][1]:
            planned_events.append(event)
            break
    # Вывод количества запланированных мероприятий и время окончания последнего из них
    print(len(planned_events), planned_events[-1][1])