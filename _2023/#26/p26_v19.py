# На производстве станок с ЧПУ обрабатывал некоторый набор деталей. В каждый момент времени станок может обрабатывать
# только одну деталь. Каждая деталь изготавливалась в определённый промежуток времени с момента начала рабочего дня.
# Простоем считается временной участок, в течение которого не обрабатывается ни одна деталь. Инженер решил узнать,
# какова суммарная длительность простоев за день и какова длительность наибольшего простоя. Общая длительность рабочего
# дня L секунд.
# Входные данные представлены в файле 26-76.txt следующим образом. В первой строке входного файла находятся два числа
# через пробел: число L – общая длина рабочего дня (натуральное число, не превышающее 109) и число N – количество
# изготовленных деталей (натуральное число, не превышающее 10 000). В следующих N строках находится по два числа через
# пробел. Первое число – время начало обработки от начала рабочего дня (натуральное число, не превышающее 109). Второе
# число – время окончания обработки (натуральное число, не превышающее 109).
# Запишите в ответе два числа: суммарную длительность простоев за день и длительность наибольшего простоя.
# Пример входного файла:
# 1000 4
# 600 750
# 350 450
# 0 350
# 950 1000
# При таких условиях имеется два простоя: 450–600; 750–950. Их суммарная длительность 350, наибольший имеет длину 200.
# Ответ: 350 200.
#
# Ответ: 1544 100

with open('26-76.txt') as f:
    day = int(f.readline().split()[0])
    data = sorted([tuple(int(y) for y in x.split()) for x in f.readlines()])
    work_ended = 0  # Время окончания работы станка
    total_rest = 0  # Общее время простоя
    max_rest = 0    # Максимальный простой

    for d in data:
        # Проверка данных
        if d[0] > day or d[1] > day:
            print('Error:', d)
        # Время простоя после окончания предыдущей работы станка
        rest = d[0] - work_ended
        # Учёт зафиксированного простоя
        if rest > 0:
            total_rest += rest
            max_rest = max(max_rest, rest)
        # Обновление времени окончания работы станка
        work_ended = d[1]

    print(total_rest, max_rest)
