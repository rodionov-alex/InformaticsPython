f = open("26_1.txt")
lines = f.readlines()[1:]  # В данном случае первая строка не нужна
f.close()

tickets = []  # Список билетов

# Запонить список билетов
for line in lines:
    splited = line.split(' ')

    if len(splited) == 2:
        r = int(splited[0])  # Ряд
        p = int(splited[1])  # Место
        ticket = (r, p)      # Билет = tuple(ряд, место)
        tickets.append(ticket)

# Сортировка по убыванию
tickets.sort(reverse=True)

res_r = 0  # Результат - ряд
res_p = 0  # Результат - место

row = 0      # Текущий ряд
places = []  # Зянятые места в ряду

# Перебор билетов
for t in tickets:
    r = t[0]
    p = t[1]

    # Если изменился ряд или билет послетний - анализируем
    if row != r or tickets.index(t) == len(tickets) - 1:
        # Анализ мест
        places.sort()  # Сортировка мест по возрастанию
        for j in range(len(places) - 1):
            if places[j + 1] - places[j] == 3:  # Пример: между 6 и 3 два места, но 6 - 3 = 3
                res_r = row
                res_p = places[j] + 1
                break

        row = r         # Обновить номер текущей строки
        places.clear()  # Очистить список мест

    # Если есть результат - прерываем цикл
    if res_r != 0:
        break

    # Добавить место в список мест ряда
    places.append(p)

print(res_r, res_p)
