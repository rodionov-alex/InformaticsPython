# -=-=-= УСЛОВНЫЙ ОПЕРАТОР if =-=-=-
print('Введите a:')
a = int(input())
print('Введите b:')
b = int(input())
print()
print('a =', a)
print('b =', b)
print()


if a > b:
    print('a > b')
if a < b:
    print('a < b')
if a == b:
    print('a == b')

print()

if a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    print('a == b')

print()

print('-=-=-= СЛОЖНЫЕ УСЛОВИЯ =-=-=-')

# Сложные условия используют логические операторы: or, and, not

if a > 0 and a > b:
    print('a > 0 and a > b')
elif 0 < a < b:  # a > 0 and a < b
    print('a > 0 and a < b')
elif 0 > a > b:  # a < 0 and a > b
    print('a < 0 and a > b')
elif a < 0 and a < b:
    print('a < 0 and a < b')
elif a == 0 and a < b:
    print('a == 0 and a < b')
elif a == 0 and a > b:
    print('a == 0 and a > b')
else:
    print('a == b == 0')


# -=-=-= ПРОТИВОПОЛОЖНОСТЬ ЗНАКОВ СРАВНЕНИЯ =-=-=-

# Любому строгому знаку неравенстрва противоположен НЕ строгий, и наоборот,
# любому НЕ строгому знаку неравенстрва противоположенн строгий.
#
# Пример:
# not (a > b) эквивалентно a <= b
# not (a >= b) эквивалентно a < b
