# Проверка, является ли число простым
def is_simple(num):
    # Число 2 является простым
    if num == 2:
        return True

    # Если число делится на 2, то оно не простое
    if num % 2 == 0:
        return False

    # Правая граница для поиска делителей
    sqrt_d = int(num ** 0.5)

    # Поиск делителей среди нечетных чисел
    for i in range(3, sqrt_d + 1, 2):
        if num % i == 0:
            return False

    # Если делителей не найдено, то число простое
    return True


count = 4   # Количество чисел, которые надо найти
n = 650000  # Число, с которого начинается поиск

# Продолжать поиск пока не найдено count чисел
while count > 0:
    n += 1                  # Инкремент
    divs = []               # Список делиелей
    rBound = int(n ** 0.5)  # Правая граница для поиска делителей

    # Перебор делителей
    for d in range(2, rBound + 1):
        if n % d == 0:
            # Если делитель простой - добавить в список
            if is_simple(d):
                divs.append(d)

            d2 = n // d  # Второй (противоположный делитель)

            # Если делитель простой - добавить в список
            if d2 != d and is_simple(d2):
                divs.append(d2)

    avg = 0  # Среднее арифметическое делителей
    divs_count = len(divs)

    if divs_count > 0:
        avg = sum(divs) // divs_count

    # Проверка, что при делении на 37, остаток равен 23
    if avg % 37 == 23:
        print(n, avg, divs)  # Вывод результата
        count -= 1           # Декремент
