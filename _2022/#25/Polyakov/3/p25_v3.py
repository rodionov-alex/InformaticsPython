# Поиск минимального делителя, заканчивающегося на 18 и не равного 18
def find_div_end8(num):
    sqrt_d = int(num ** 0.5)  # Делитель - целое от корня из num
    d = 2                     # Текущий делитель
    min_d2 = num              # Наименьший делитель из второй половины, заканчивающийся на 18

    # Продолжать поиск делителей пока текущий делитель меньше корня из num
    while d <= sqrt_d:
        # Если найден делитель
        if num % d == 0:
            d2 = num // d  # Делитель из второй половины (противоположный первому)

            # Если делитель из первой половины оканчивается на 18
            if d % 10 == 8 and d > 8:
                return d  # то он будет наименьшим и надо вернуть его
            # Иначе если делитель из второй половины заканчивается на 18 и меньше наименьшего
            elif d2 % 10 == 8 and 8 < d2 < min_d2:
                min_d2 = d2  # то то наименьшим становится делитель d2
        d += 1  # Инкремент

    # Если cписок делителей из второй половины не пустой, то вернем минимальный
    if min_d2 < num:
        return min_d2

    # Если делитель не найден - вернуть 0
    return 0


n = 500000  # Число, с которого начинается поиск
count = 5   # Количество чисел, которые надо найти

# Продолжать поиск пока не найдено count чисел
while count:
    n += 1                  # Инкремент
    res = find_div_end8(n)  # Поиск минимального делителя, заканчивающегося на 18

    if res != 0:
        print(n, res)  # Вывод результата
        count -= 1     # Декремент
    