import time

start = time.time()


# Бинарный поиск подходящего куска оптоволокна
# cuts_list - массив кусков оптоволокна, должен быть отсортирован по возрастанию
# min_cut_len - минимальная необходимая длина куска оптоволокна
def find_suitable_cut(cuts_list, min_cut_len):
    index_start = 0                 # Левая граница
    index_end = len(cuts_list) - 1  # Правая граница
    suitable_cut_index = index_end  # Индекс подходящего куска оптоволокна, по умолчанию самый большой

    # Продолжать поиск пока границы не сойдутся
    while index_start <= index_end:
        # На левой границе кусок точно подходящей длины
        if min_cut_len == cuts_list[index_start]:
            return index_start
        # На правой границе кусок точно подходящей длины
        if min_cut_len == cuts_list[index_end]:
            return index_end

        # Если минимальная необходимая длина куска оптоволокна меньше куска на левой границе,
        # то индекс подходящего отрезка переместить на левую границу
        if (min_cut_len <= cuts_list[index_start]) and (suitable_cut_index != index_start):
            suitable_cut_index = index_start

        # Срейдний индекс
        index_mid = (index_start + index_end) // 2
        # Если необходимый кусок находится левее середины, то сдвинуть правую границу
        if min_cut_len < cuts_list[index_mid]:
            index_end = index_mid - 1
            # Если подходящий кусок не находится слева от левой границы,
            # то его необходимо сдвинуть на index_mid
            if suitable_cut_index != index_start:
                suitable_cut_index = index_mid
        # Если необходимый кусок находится правее середины, то сдвинуть левую границу
        elif min_cut_len > cuts_list[index_mid]:
            index_start = index_mid + 1
        # Ровно по середине находится кусок точно подходящей длины
        else:
            return index_mid

    # Вернуть индекс подходящего куска оптоволокна, если не нашелся кусок точной длины
    return suitable_cut_index


f = open('26_2.txt')
lines = f.readlines()
f.close()
target_length = int(lines[0].split(' ')[1])  # Необходимая длина оптоволокна
cuts = [int(i) for i in lines[1:]]           # Массив кусков оптоволокна
cuts.sort()                                  # Сортировка кусков по возрастанию
cuts_length = sum(cuts)                      # Сумма длин всех кусков оптоволокна
weldings = 0                                 # Общее количество сварок
count = 0                                    # Количество полученных кусков требуемой длины

# Подсчет оптоволокна
while cuts_length >= target_length:
    used_cuts_length = cuts.pop()  # Длина использованных кусков оптоволокна (берётся последний, самый длинный)
    used_cuts = 1                  # Количество использованных кусков оптоволокна

    # Подсчет необходимого количества кусков оптоволокна для требуемой длины
    while used_cuts_length < target_length:
        index = find_suitable_cut(cuts, target_length - used_cuts_length)  # Поиск индекса подходящего куска
        used_cuts_length += cuts.pop(index)                                # Добавить найденный кусок оптоволокна
        used_cuts += 1                                                     # Инкремент кусков оптоволокна

    # Подсчет количества швов
    if used_cuts > 1:
        weldings += used_cuts - 1

    residue = used_cuts_length - target_length  # Остаток от спаянных кусков оптоволокна
    cuts_length -= target_length                # Изменение длины оставшихся кусков оптоволокна
    count += 1                                  # Инкремент количества полученных кусков требуемой длины

    # Положить остаток в массив кусков оптоволокна
    if residue > 0:
        cuts.append(residue)
        cuts.sort()

# Результат
print(weldings, len(cuts))

end = time.time()
total = end - start
print("%.3f" % total, "sec.")
