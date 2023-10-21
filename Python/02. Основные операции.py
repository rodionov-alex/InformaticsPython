print('-=-=-= ОСНОВНЫЕ ОПЕРАЦИИ =-=-=-')

x = 14
print('x =', x)
y = 5
print('y =', y)
# Сумма, +
z = x + y
print('x + y =', z)
# Разность, -
z = x - y
print('x - y =', z)
# Произведение, *
z = x * y
print('x * y =', z)
# Частное, /
z = x / y
print('x / y =', z)
# Остаток от деления, %
z = x % y
print('x % y =', z)
# Деление без остатка, //
z = x // y
print('x // y =', z)
# Возведение в степень, **
z = y ** 3
print('y ** 3 =', z)


print('-=-=-= ОПЕРАЦИИ ПРИСВАИВАНИЯ =-=-=-')

# Присвоить
x = 14
print('x =', x)
y = 5
print('y =', y)
# Операция присваивания + основные операции
x += 3  # Интерпретируется как x = x + 3
print('x += 3  ->  x =', x)
x -= 3  # Интерпретируется как x = x - 3
print('x -= 3  ->  x =', x)
# Аналогично воможно использование с остальными основными операциями: *, /, % и т.д.
print()


print('-=-=-= ОПЕРАЦИИ СРАВНЕНИЯ =-=-=-')

# Больше, >
print('x > y =', x > y)
# Меньше, <
print('x < y =', x < y)
# Больше или равно, >=
print('x >= y =', x >= y)
# Меньше или равно, <=
print('x <= y =', x <= y)
# Равно, ==
print('x == y =', x == y)
# Не равно, !=
print('x != y =', x != y)
# Идентичность объектов, is
print('x is y =', x is y)
print('x is x =', x is x)
print('x is not y =', x is not y)
print('x is not x =', x is not x)
print()
# Наличие значения в списке или строке, in
arr = [4, 6, 9, 1, 3]
print('arr =', arr)
print('9 in arr =', 9 in arr)
print('5 in arr =', 5 in arr)
print('9 not in arr =', 9 not in arr)
print('5 not in arr =', 5 not in arr)
print()
s = 'Мама мыла раму'
print('s =', s)
print('\'Мама\' in s =', 'Мама' in s)
print('\'Папа\' in s =', 'Папа' in s)
print('\'Мама\' not in s =', 'Мама' not in s)
print('\'Папа\' not in s =', 'Папа' not in s)
print()


print('-=-=-= ЛОГИЧЕСКИЕ ОПЕРАЦИИ =-=-=-')

a = True
b = False
print('a =', a)
print('b =', b)
print()

# Логическое ИЛИ, or
print('a or b =', a or b)
# Логическое И, and
print('a and b =', a and b)
# Логическое ОТРИЦАНИЕ, not
print('not a =', not a)
print()


print('-=-=-= ПОБИТОВЫЕ ОПРЕАЦИИ =-=-=-')
x = 9   # 1001
y = 10  # 1010
print('x = ', x, ' (', bin(x)[2:], ')', sep='')
print('y = ', y, ' (', bin(y)[2:], ')', sep='')
print()

# Побитовое ИЛИ / OR
z = x | y
print('x | y = ', z, ' (', bin(z)[2:], '), побитовое ИЛИ', sep='')
# Побитовое И / AND
z = x & y
print('x & y = ', z, ' (', bin(z)[2:], '), побитовое И', sep='')
# Побитовое исключающее ИЛИ / XOR
z = x ^ y
print('x ^ y = ', z, ' (', bin(z)[2:], '), побитовое исключающее ИЛИ', sep='')
# Побитовое НЕ: ~x = -(x + 1)
z = ~x
print('~x = ', z, ' (-', bin(z)[3:], '), побитовое НЕ', sep='')
# Побитовый сдвиг влево
z = x << 2
print('x << 2 = ', z, ' (', bin(z)[2:], '), сдвиг на 2 бита влево', sep='')
# Побитовый сдвиг вправо
z = x >> 2
print('x >> 2 = ', z, ' (', bin(z)[2:], '), сдвиг на 2 бита вправо', sep='')
