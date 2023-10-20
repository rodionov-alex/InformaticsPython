from tqdm import tqdm


f = open("26_10.txt")
lines = f.readlines()[1:]  # В данном случае первая строка не нужна
f.close()
numbers = [int(i) for i in lines]       # Список чисел
avgs = []                               # Список средних-арифметических, найденных в списке numbers
numbers.sort()                          # Сортировка списка чисел !!!Обязательно!!!
mid_bound = numbers[len(numbers) // 2]  # Средняя граница (первое число из большей половины)

# Поиск средних-арифметических пар чисел и заполнение списка avgs
for i in tqdm(range(len(numbers) - 1)):  # tqdm - это ProgressBar, удалить если не подключена соответствующая библиотека
    for j in range(i + 1, len(numbers)):
        sm = numbers[i] + numbers[j]  # Сумма пары
        # Проверка на четность
        if sm % 2 == 0:
            avg = sm // 2
            # Проверка, меньше ли avg половины чисел списка numbers
            if avg < mid_bound:
                avgs.append(avg)

# Результат
print(len(avgs), max(avgs))
