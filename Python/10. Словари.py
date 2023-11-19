print('-=-=-= СЛОВАРИ =-=-=-')

# Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу. Их иногда ещё называют
# ассоциативными массивами или хеш-таблицами.

# Способы создания словаря:

# 1) С помощью литерала {}
d = {}
print('d =', d)
month_number = {'january': 1, 'february': 2, 'march': 3}  # ключ - строка
print('month_number =', month_number)

month_name = {1: 'january', 2: 'february', 3: 'march'}  # ключ - число
print('month_name =', month_name)


# 2) С помощью функции dict()
days_count = dict(january=31, february=28, march=31)
print("days_count =", days_count)

# 3) С помощью метода fromkeys()
d = dict.fromkeys(['x', 'y'], 10)
print('d =', d)
print()


print('-=-=-= РАБОТА СО СЛОВАРЕМ =-=-=-')

# Доступ к элементам словаря производится по ключу с помощью оператора []
print('month_number[\'february\'] =', month_number['february'])
print('month_name[1] =', month_name[1])
print('days_count[\'march\'] =', days_count['march'])
print()

# Добавление и редактирование элементов словаря так же производится по ключу с помощью оператора []. При этом,
# если в словаре уже есть указанный ключ, то обновится значение по этому ключу. А если указанного ключа нет,
# то он добавится с заданным значением.
print('month_name =', month_name)
# Ключа 4 нет в словаре и он будет добавлен со значением 'december'
month_name[4] = 'december'
print('month_name[4] = \'december\' ->', month_name)
# Ключ 4 уже есть в словаре и значение по ключу 4 обновится на 'april'
month_name[4] = 'april'
print('month_name[4] = \'april\' ->', month_name)
print()


print('-=-=-= МЕТОДЫ СЛОВАРЕЙ (ФУНКЦИИ) =-=-=-')

print("days_count =", days_count)
print()

# Возвращает копию словаря
d_copy = days_count.copy()
print('d_copy = days_count.copy() -> dcopy =', d_copy)
# Возвращает ключи в словаре
print('days_count.keys() ->', days_count.keys())
# Возвращает значения в словаре
print('days_count.values() ->', days_count.values())
# Возвращает кортежами пары (ключ, значение)
print('days_count.items() ->', days_count.items())
# Удаляет ключ и возвращает значение
print('days_count.pop(\'march\') ->', days_count.pop('march'), '| days_count =', days_count)
# Удаляет и возвращает последнюю добавленную в словарь пару (ключ, значение)
print('days_count.popitem() ->', days_count.popitem(), '| days_count =', days_count)
# Обновляет словарь, добавляя пары (ключ, значение) из другого словаря или с помощью пар: ключ=значение
days_count.update(d_copy)
print('days_count.update(d_copy) ->', days_count)
days_count.update(april=30, may=31)
print('days_count.update(april=30, may=31) ->', days_count)
# Возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None)
print('days_count.get(\'februaury\') ->', days_count.get('februaury'))
# !!! Метод get() использовать в алгоритмах сравнения, например в функции min или max. По умолчанию эти функции
# будут искать наименьшее или наибольшее не среди значений, а среди ключей.
print('min(days_count) ->', min(days_count))  # В данном случае результатом будет 'april' т.к. он начинается с буквы a
# А если в качестве аргумента key в функцию min() отдать метод get(), то функция будет использовать его для
# сравнений и искать минимум уже среди значений словаря. Но обратите внимание, что хоть и сравнивать она будет
# значения, но вернет в качестве результата все равно ключ. Таким образом можно определить в словаре месяц с наименьшим
# количесвом дней.
print('min(days_count, key=days_count.get) ->', min(days_count, key=days_count.get))
# Очищает словарь
days_count.clear()
print('days_count.clear() =>', days_count)
