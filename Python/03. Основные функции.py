import math

# -=-=-= ФУНКЦИИ ВВОДА / ВЫВОДА =-=-=-

# Для вывода информации в консоль используется функция print(). В качестве аргументов этой функции
# можно передавать разные данные (строки, числа, списки и пр.) через запятую, при этом выводимые
# данные будут разделяться сепаратором (разделителем), которым по умолчанию является пробел. Его
# можно поменять, задав последним агрументом: sep='_'.
# Пример:
# print('Привет','мир', sep='_')  # выведет на экран: Привет_мир
#
# Для ввода данных используется функция input(), которая ожидает когда пользователь введет их с клавиатуры,
# а затем возвращает в виде строки. Поэтому если нужно ввести числовые данные, то их нужно будет преобразовать
# к числовым. Пример: a = int(input()).


print('-=-=-= МАТЕМАТИЧЕСКИЕ ФУНКЦИИ =-=-=-')

# pow(x, exp) - возведение в степень.
# Функция возводит число x в степень exp.
print('pow(2, 8) =', pow(2, 8))

# abs(x) - модуль (абсолючное значение) числа.
# Функция возвращает модуль числа x.
print('abs(-5) =', abs(-5))

# max(arg1, arg2, args...), max(iterable) - максимальное значение
# Функция возвращает максимальное значение (максимальный элемент списка)
print('max(2, 6, 4) =', max(2, 6, 4))
print('max([2, 6, 4]) =', max([2, 6, 4]))

# min(arg1, arg2, args...), max(iterable) - максимальное значение
# Функция возвращает минимальное значение (минимальный элемент списка)
print('min(2, 6, 4) =', min(2, 6, 4))
print('min([2, 6, 4]) =', min([2, 6, 4]))
print()

# Для функций min и max в качестве аргумета key= можно отдать функцию (или лямбду) для специфичного сравнения элементов.
# Пример определения кортежа, у которого элемент под индексом 1 является максимальным/минимальным.
tuples = [(4, 7), (9, 2), (5, 9)]
print('tuples =', tuples)
print('max(tuples) =', max(tuples))
print('max(tuples, key=lambda x: x[1]) =', max(tuples, key=lambda x: x[1]))
print('min(tuples) =', min(tuples))
print('min(tuples, key=lambda x: x[1]) =', min(tuples, key=lambda x: x[1]))
print()

# math.gcd(x, y) - наибольший общий делитель (greatest common divisior). (Функция из библиотеки math)
# Функция возвращает наибольший общий делитель двух чисел.
print('math.gcd(256, 80) =', math.gcd(256, 80))
# math.lcm(x, y) - наименьший общий множитель (least common multiple). (Функция из библиотеки math)
print('math.lcm(256, 80) =', math.lcm(256, 80))
print()

# Так же множество математических функций можно найти в библиотеке math:
# sin(), cos(), tan(), log(), factorial(), radians(), pi и многи другие...


print('-=-=-= ФУНКЦИИ СРАВНЕНИЯ =-=-=-')
arr1 = [0, 1, 0, 1]
arr2 = [1, 1, 1, 1]
arr3 = [0, 0, 0, 0]
print('arr1 =', arr1)
print('arr2 =', arr2)
print('arr3 =', arr3)
# all(iterable) - возвращает истину если все элементы последовательности возвращают истину.
print('all(arr1) =', all(arr1))
print('all(arr2) =', all(arr2))
print('all(arr3) =', all(arr3))
# any(iterable) - возвращает истину если хотя бы один элемент последовательности возвращает истину.
print('any(arr1) =', any(arr1))
print('any(arr2) =', any(arr2))
print('any(arr3) =', any(arr3))
print()


print('-=-=-= ФУНКЦИИ ОКРУГЛЕНИЯ =-=-=-')

x = 2.4567
print('x =', x)
print()

# round(number, digits) - округление вещественного числа.
# Функция округляет число number до digits знаков после запятой. По умолчанию digits = 0.
print('round(x) =', round(x))
print('round(x, 2) =', round(x, 2))  # округление до 2 знаков после запятой
# math.floor(x) - округление вещественного числа в меньшую сторону. (Функция из библиотеки math)
# Функция округляет число x в меньшую сторону. Обратить внимание на отрицательные числа.
print('math.floor(x) =', math.floor(x))
print('math.floor(-x) =', math.floor(-x))
# math.ceil(x) - округление вещественного числа в большую сторону. (Функция из библиотеки math)
# Функция округляет число x в большую сторону. Обратить внимание на отрицательные числа.
print('math.ceil(x) =', math.ceil(x))
print('math.ceil(-x) =', math.ceil(-x))
# math.trunc(x) - убрать дробную часть вещественного числа. (Функция из библиотеки math)
# Функция не округляет, а убирает именно дробную часть вещественного числа.
print('math.trunc(x) =', math.trunc(x))
print('math.trunc(-x) =', math.trunc(-x))
print()


print('-=-=-= ФУНКЦИИ ПЕРЕВОДА В ДРУГИЕ СИСТЕМЫ СЧИСЛЕНИЯ =-=-=-')

# Функции перевода в другие системы счисления в качвестве результата возвращают СТРОКУ,
# первый символ которой равен '0', второй символ характеризует систему счисления числа, а
# остальные - значение числа в этой системе счисления.
# b - bin / двоичная
# o - oct / восьмиричная
# x - hex / шестнадцатиричная

# Перевод в двоичную с/с
print('bin(165) =', bin(165))
# Перевод в восьмиричную с/с
print('oct(165) =', oct(165))
# Перевод в шестнадцатиричную с/с
print('hex(165) =', hex(165))

# Функция int() может использоваться для перевода из другой системы счисления (вплоть до 36-ричной = 10 цифр + 26 букв)
# в десятичную систему счисления. Для этого в качестве первого аргумента ей отдается строковое представление числа, а
# вторым указывается его система счисления. В отличие от предыдущих функций, функция int() на выходе возвращает число,
# а не строку.

# Перевод из двоичной системы счисления в десятичную
print('int(\'1001\', 2) =', int('1001', 2))
# Перевод из тридцатишестиричной системы счисления в десятичную
print('int(\'54qwe\', 36) =', int('54qwe', 36))

# Ошибка: нельзя преобразовать строку с буквами к целочисленному числу без указания основания системы счисления.
# print(int('54qwe'))
print()


print('-=-=-= ФУНКЦИИ СОЗДАНИЯ И ПРЕОБРАЗОВАНИЯ ТИПОВ =-=-=-')

# int(float), int(str, int) - функция преобразования к целочисленному типу.
print('float -> int:\tint(5.467) =', int(5.467))    # преобразует вещественное число в целочисленное
print('str -> int:\t\tint(\'256\') =', int('256'))  # преобразует строку в целочисленное число

# Ошибка: нельзя преобразовать строку с вещественным числом к целочисленному числу.
# print(int('5.467'))
print()

# float(int), float(str) - функция преобразования к вещественному типу.
print('int -> float:\tfloat(5) =', float(5))                # преобразует целочисленное число в вещественное
print('str -> float:\tfloat(\'5.467\') =', float('5.467'))  # преобразует строку в вещественное число
print('float(\'inf\') =', float('inf'))                     # возвращает максимально большое число (бесконечность)
print('float(\'-inf\') =', float('-inf'))                   # возвращает минимальное число (минус бесконечность)

# Ошибка: нельзя преобразовать строку с буквами к вещественному числу
# print(float('54qwe'))
print()

# bool(int) - функция преобразования к булевому типу.
print('int -> bool:\tbool(4) =', bool(4))
print('int -> bool:\tbool(0) =', bool(0))
print('float -> bool:\tbool(-4.4) =', bool(-4.4))
print()

# list(itrable) - функция преобразования в список.
# Функция принимает итерируемый объект и преобразует его в список. Если вызвать без аргумента - вернет пустой список.
print('list((1, 2, 3)) =', list((1, 2, 3)))  # преобразует кортеж в список
print('list() =', list())                    # создает пустой список
print()

# tuple(itrable) - функция преобразования в кортеж.
# Функция принимает итерируемый объект и преобразует его в кортеж.
print('tuple([1, 2, 3]) =', tuple([1, 2, 3]))  # преобразует список в кортеж
print()

# set(itrable) - функция преобразования в множество.
# Функция принимает итерируемый объект и преобразует его в множество.
# Если вызвать без аргумента - вернет пустое множество.
print('set([2, 4, 2]) =', set([2, 4, 2]))  # преобразует список в множество, при этом удалит повторяющиеся элементы
print('set() =', set())                    # создает пустое множество
print()

# dict(**kwargs), dict(itrable), dict(mapping) - функция создания словаря.
print('dict(one=1, two=2, three=3)\t\t\t\t\t =', dict(one=1, two=2, three=3))
print('dict([(\'one\', 1), (\'two\', 2), (\'three\', 3)]) =', dict([('one', 1), ('two', 2), ('three', 3)]))
print('dict({\'one\': 1, \'two\': 2, \'three\': 3})\t\t =', dict({'one': 1, 'two': 2, 'three': 3}))
print()


print('-=-=-= ФУНКЦИИ ОБРАБОТКИ iterable ОБЪЕКТОВ =-=-=-')

# sum(iterable) - сумма элементов списка.
# Функция вычисляет сумму элементов списка (или других итеррируемых объектов).
print('sum([2, 5, 9, 3]) =', sum([2, 5, 9, 3]))

# len(iterable) - длина списка.
# Функция возвращает количество элементов списка (или других итеррируемых объектов).
print('len([2, 5, 9, 3]) =', len([2, 5, 9, 3]))
print()

# sorted(iterable) - сортировка списка.
# Функция возвращает сортированный список (или другиой итеррируемый объект).
# По умолчанию функциясортирует по возрастанию, для сортировки по убыванию необходимо задать аргумет reverse=True.
arr = [6, 2, 9, 3, 7, 1, 4, 5, 0, 8]
print('arr =', arr)
print('sorted(arr) =', sorted(arr))
print('sorted(arr, reverse=True) =', sorted(arr, reverse=True))
print()

# enumerate(iterable) - счетчик элементов последовательности в циклах.
# Функция возвращает список кортежей вида: (индекс_элемента, значение_элемента).
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
print('seasons =', seasons)
print('enumerate(seasons) ->', *(enumerate(seasons)))
print()

# zip(iterables) - упаковка списков (или других итеррируемых объектов).
# Функция склеивает в кортежи соответствующие элементы переданных ей аргументов: нулевой с нулевыми,
# первй с первыми и т.д. и возвращает их в виде списка.
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print('arr1 =', arr1, ', arr2 =', arr2)
print('zip(arr1, arr2) ->', *(zip(arr1, arr2)))
print()

# map(func, iterable) - применение функции (или лямбды) к каждому элементу списка (или другому итеррируемуму объекту).
# Функция возвращает копию списка, где каждому элементу применена переданная в качестве аргумента функция.
arr = ['123', '456', '789']
print('arr =', arr)
print('map(int, arr) ->', *(map(int, arr)))  # применяет функцию int() к каждому элементу списка arr
print()

# filter(func, iterable) - фильтрация элементов списка (или другого итеррируемого объекта).
# Функция возвращает отфильтрованный по определенному правилу список. Правило фльтрации можно задать с помощью
# функции или лямбды.
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('arr =', arr)
print('filter(lambda x: x % 2 == 0, arr) ->', *(filter(lambda x: x % 2 == 0, arr)))  # фильтр на четность
print()
