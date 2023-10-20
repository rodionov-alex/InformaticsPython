from string import ascii_uppercase

print('-=-=-= Перевод в систему счисления =-=-=-')
# Возвращает в виде строки значение числа n в системе счисления с основанием base.
def to_ss(n: int, base: int):
    res = ''

    # Максимальное основание 36 = 10 цифр + 26 букв
    if base <= 36:
        while n:
            ost = n % base   # Остаток от деления на основание системы счисления
            # Остатки больше 9 записываются буквами
            ost = str(ost) if ost < 10 else ascii_uppercase[ost - 10]
            res = ost + res  # Добавление остатка в начало
            n //= base       # Деление без остатка

    return res

print('to_ss(12, 2) =', to_ss(12, 2))
print('to_ss(3978, 16) =', to_ss(3978, 16))
# P.S. для перевода в десятичную систему счисления используется функция int()
print('int(to_ss(3978, 16), 16) =', int(to_ss(3978, 16), 16))
print()


print('-=-=-= Простое число =-=-=-')
# Возвращает True если число n простое, в противном случае - False.
def is_simple(n: int):
    # Все четные числа - не простые, кроме 2
    if n % 2 == 0:
        return n == 2
    # Перебор нечетных делителей
    for d in range(3, int(n ** 0.5) + 1, 2):
        if n % d == 0:
            return False
    # Если делителей не нашлось, значит n - простое число
    return True

print('is_simple(15) =', is_simple(15))
print('is_simple(17) =', is_simple(17))
print()


print('-=-=-= Поиск делителей числа =-=-=-')
# Возвращает список всех делителей числа n кроме 1 и самого числа.
def get_divs(n: int):
    res = set()  # set - чтобы удалить дубликат от корня
    # Перебор потенциальных делителей числа от 1 до корня из числа
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            res.add(d)       # Добавить делитель
            res.add(n // d)  # Добавить частное
    # Возвращение результата в виде списка
    return list(res)

print('get_divs(36) =', get_divs(36))
print()


print('-=-=-= Бинарный поиск =-=-=-')
# Возвращает True - если элемент val найден в списке elements, False - в противном случае.
def bin_search(val, elements):
    elements = sorted(elements)    # Список должен быть обязательно отсортирован
    index_start = 0                # Индекс начала
    index_end = len(elements) - 1  # Индекс конца

    # Продолжать поиск пока индекс начала и конца не "пересеклись"
    while index_start <= index_end:
        # Если искомое значение лежит на границе поиска
        if (val == elements[index_start]) or (val == elements[index_end]):
            return True
        # Индекс середины
        index_mid = (index_start + index_end) // 2
        # Если искомое значение находится слева от середины - двигаем конец поиска на середину
        if val < elements[index_mid]:
            index_end = index_mid - 1
        # Если искомое значение находится справа от середины - двигаем начало поиска на середину
        elif val > elements[index_mid]:
            index_start = index_mid + 1
        # Искомое находится на середине
        else:
            return True

    # Искомое не было найдено
    return False

arr = [16, 5, 8, 90, 44, 17, 81, 2, 77, 22, 13, 19, 51, 74]
print('arr =', arr)
print('bin_search(77, arr) =', bin_search(77, arr))
print('bin_search(75, arr) =', bin_search(75, arr))
print()
