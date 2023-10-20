from tqdm import tqdm


# Бинарный поиск.
# Поиск значения val в списке elements. !!!Список должен быть сортированный!!!
def BinSearch(val, elements):
    index_start = 0
    index_end = len(elements) - 1

    while index_start <= index_end:
        if (val == elements[index_start]) or (val == elements[index_end]):
            return True

        index_mid = (index_start + index_end) // 2

        if val < elements[index_mid]:
            index_end = index_mid - 1
        elif val > elements[index_mid]:
            index_start = index_mid + 1
        else:
            return True

    return False


f = open("26_5.txt")
lines = f.readlines()[1:]  # В данном случае первая строка не нужна
f.close()
numbers = [int(i) for i in lines]  # Список чисел
numbers.sort()                          # Сортировка списка чисел !!!Обязательно!!!
# numbers = set(int(i) for i in lines)  # Список чисел
even = [x for x in numbers if x % 2 == 0]  # Список четных чисел
avgs = []                                  # Список средних-арифметических, найденных в списке numbers

# Поиск средних-арифметических пар чисел и заполнение списка avgs
for i in tqdm(range(len(even) - 1)):  # tqdm - это ProgressBar, удалить если не подключена соответствующая библиотека
    for j in range(i + 1, len(even)):
        avg = (even[i] + even[j]) // 2

        # Проверка, находится ли avg в списке numbers
        if BinSearch(avg, numbers):
        # if avg in numbers:
            avgs.append(avg)

print(len(avgs), min(avgs))
