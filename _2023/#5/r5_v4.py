# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля). По этому числу строится
# новое число по следующим правилам.
# 1. Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
# 2. Наименьшая из полученных трёх сумм удаляется.
# 3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
# Пример. Исходное число: 1984. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 4 = 12. Удаляется 10. Результат: 1217.
# Укажите наибольшее число, при обработке которого автомат выдаёт результат 613.
# Примечание. Если меньшие из трех сумм равны, то отбрасывают одну из них.
#
# Ответ: 9424

for n in range(9999, 999, -1):
    digits = [int(x) for x in str(n)]
    r = [digits[0] + digits[1], digits[1] + digits[2], digits[2] + digits[3]]
    r.remove(min(r))
    r.sort()
    r = ''.join([str(x) for x in r])

    if r == '613':
        print(n)
        break
