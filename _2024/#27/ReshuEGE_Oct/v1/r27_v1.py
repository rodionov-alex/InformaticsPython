# Имеется набор данных, состоящий из троек положительных целых чисел. Необходимо выбрать из каждой тройки
# ровно одно число так, чтобы сумма всех выбранных чисел не делилась на k = 109 и при этом была максимально
# возможной. Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число —
# максимально возможную сумму, соответствующую условиям задачи.
#
# Входные данные.
# Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество троек
# N (1 ≤ N ≤ 1 000 000). Каждая из следующих N строк содержит три натуральных числа, не превышающих 20 000.
#
# Пример организации исходных данных во входном файле:
# 6
# 1 3 7
# 5 12 6
# 6 9 11
# 5 4 8
# 3 5 4
# 1 1 1
#
# Для указанных входных данных, в случае, если k = 5, значением искомой суммы является число 44.
# В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.
#
# Ответ: 784594 8819088760

with open('27_A.txt') as f:
    k = 109
    n = int(f.readline())
    data = [tuple(sorted(map(int, x.split()), reverse=True)) for x in f.readlines()]
    min_dif = float('inf')  # минимальная не кратьная k разница с максимальным элементом в тройках
    mx_sum = 0

    for d in data:
        mx_sum += d[0]
        r1 = d[0] - d[1]  # Разница максимального в тройке с первым элементом
        r2 = d[0] - d[2]  # Разница максимального в тройке со вторым элементом

        if r1 < min_dif and r1 % k:
            min_dif = r1
        elif r2 < min_dif and r2 % k:
            min_dif = r2

    # Если максимальная сумма получается кратной k, то из нее надо вычесть
    # минимальную не кратьную k разницу с максимальным элементом в тройках.
    if mx_sum % k == 0:
        mx_sum -= min_dif

    print(mx_sum)