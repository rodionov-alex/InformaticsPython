# Входной файл содержит сведения о заявках на проведение мероприятий
# в конференц-зале. В каждой заявке указаны время начала и время окончания
# мероприятия (в минутах от начала суток). Если время начала одного
# мероприятия меньше времени окончания другого, то провести можно только
# одно из них. Если время окончания одного мероприятия совпадает
# со временем начала другого, то провести можно оба. Определите, какое
# максимальное количество мероприятий можно провести в конференц-зале
# и каков при этом максимально возможный перерыв между двумя
# последними мероприятиями.
# Входные данные
# В первой строке входного файла находится натуральное число N (N ≤ 1000) –
# количество заявок на проведение мероприятий. Следующие N строк
# содержат пары чисел, обозначающих время начала и время окончания
# мероприятий. Каждое из чисел натуральное, не превосходящее 1440.
# Запишите в ответе два числа: максимальное количество мероприятий
# и самый длинный перерыв между двумя последними мероприятиями
# (в минутах).
# Типовой пример организации данных во входном файле
# 5
# 10 150
# 100 120
# 131 170
# 150 180
# 120 130
# При таких исходных данных можно провести максимум три мероприятия,
# например, мероприятия по заявкам 2, 3 и 5. Максимальный перерыв между
# двумя последними мероприятиями составит 20 мин., если состоятся
# мероприятия по заявкам 2, 4 и 5.
# Типовой пример имеет иллюстративный характер. Для выполнения
# задания используйте данные из прилагаемых файлов.

with open('Task/Доп_файлы/Задание 26/26_2024.txt') as f:
    events = [tuple(map(int, x.split())) for x in f.readlines()[1:]]
    events.sort(key=lambda x: x[1])  # сортировка по возрастанию по окончаниям мероприятий
    events_on_timeline = [events[0]]

    # Расстановка мероприятий по таймлайну в порядке возрастания окончаний мероприятий
    for i in range(1, len(events)):
        # Добавить очередное мероприятие если его началу не мешает последнее мероприятие на таймлайне
        if events[i][0] >= events_on_timeline[-1][1]:
            events_on_timeline.append(events[i])

    # Сортируем по убыванию, чтобы в начале оказалось мероприятие с самым поздним стартом
    events.sort(key=lambda x: x[0], reverse=True)

    # Выводим количество мероприятий на таймлайне и разницу между началом самого
    # позднего мероприятия и концом предпоследнего мероприятия на таймлайне.
    print(len(events_on_timeline), events[0][0] - events_on_timeline[-2][1])

# Ответ: 32 15
