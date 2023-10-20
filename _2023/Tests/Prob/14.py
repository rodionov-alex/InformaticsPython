# Операнды арифметического выражения записаны в системе счисления с основанием 15.
# 99658x29(15) + 102x023(15)
# В записи чисел переменной х обозначена неизвестная цифра из алфавита 15-ричной системы счисления. Определите
# наибольшее значение х, при котором значение данного арифметического выражения кратно 14. Для найденного
# значения х вычислите частное от деления значения арифметического выражения на 14 и укажите его в ответе в
# десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.
#
# Ответ: 118330623

alf = '0123456789ABCDE'

for x in alf:
    n1 = int('99658{}29'.format(x), 15)
    n2 = int('102{}023'.format(x), 15)
    sm = n1 + n2
    if sm % 14 == 0:
        print(sm // 14)