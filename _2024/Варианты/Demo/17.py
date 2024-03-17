with open('Task/Доп_файлы/Задание 17/17_2024.txt') as f:
    data = list(map(int, f.readlines()))
    # Максимальное число оканчивающееся на 13
    mx13 = max(data, key=lambda x: x if str(x).endswith('13') else 0)
    mx_sum = 0
    count = 0

    # Перебор троек, i-й индекс указывает на последнее число тройки
    for i in range(2, len(data)):
        triple = data[i - 2:i + 1]
        # Длины чисел
        triple_lens = list(map(len, [str(x) for x in triple]))

        if triple_lens.count(3) == 2:
            sm = sum(triple)

            if sm < mx13:
                mx_sum = max(sm, mx_sum)
                count += 1

    print(count, mx_sum)

# Ответ: 959 97471
