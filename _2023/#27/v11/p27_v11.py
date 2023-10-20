# На вход программе поступает последовательность натуральных чисел. Рассматриваются все непрерывные
# подпоследовательности исходной последовательности, сумма элементов которых кратна K, и при этом
# сумма чисел, не вошедших в подпоследовательность, кратна D. Найти количество таких подпоследовательностей.
# Входные данные. Даны два входных файла (файл A и файл B), содержит в первой строке натуральное число
# N (2 ≤ N ≤ 5 000 000) – количество чисел в последовательности, число K и число D. Каждая из следующих
# N строк содержит одно натуральное число, не превышающее 10000.
# Пример входного файла:
# 5 2 3
# 5
# 1
# 9
# 16
# 4
# В этой последовательности можно выбрать две подходящих подпоследовательности: {1, 9, 16} (сумма элементов
# последовательности 26 кратна K = 2 и сумма оставшихся элементов 9 кратна D = 3; 2)) и {16, 4} (сумма элементов
# последовательности 20 кратна K = 2 и сумма оставшихся элементов 15 кратна D = 3). Ответ: 2.
# В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
#
# Ответ: 149 249464

from tqdm import tqdm

# A
# with open('27-116b.txt') as f:
#     n, k, d = tuple(map(int, f.readline().split()))
#     data = list(map(int, f.readlines()))
#     total_sum = sum(data)
#     mx_len = n - 1
#     sequences = [x for x in data if x % k == 0]
#     count = 0
#
#     for ln in tqdm(range(2, mx_len)):
#         for i in range(n - (ln - 1)):
#             sm = sum(data[i:i + ln])
#
#             if sm % k == 0:
#                 sequences.append(sm)
#
#     for s in sequences:
#         if (total_sum - s) % d == 0:
#             count += 1
#
#     print(count)


# B
with open('27-116b.txt') as f:
    n, k, d = tuple(map(int, f.readline().split()))
    data = list(map(int, f.readlines()))
    total_sum = sum(data)
    mx_len = n - 1
    sums = data.copy()
    sequences = [x for x in data if x % k == 0]
    count = 0

    for ln in tqdm(range(2, mx_len)):
        for i in range(n - ln + 1):
            sums[i] += data[i + (ln - 1)]

            if sums[i] % k == 0:
                sequences.append(sums[i])

    for s in sequences:
        if (total_sum - s) % d == 0:
            count += 1

    print(count)


