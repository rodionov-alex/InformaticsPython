# Перевод числа в семеричную систему счисления
def to_7th(num):
    res = ''

    while num != 0:
        res = str(num % 7) + res
        num //= 7

    return res


f = open('17_7.txt')
lines = f.readlines()
f.close()
nums = [int(n) for n in lines]  # Список чисел
nums_count = len(nums)          # Количество чисел
sums = []                       # Суммы пар в семеричной с/с

# Перебор чисел
for i in range(nums_count - 1):
    pair_sum = nums[i] + nums[i + 1]  # Сумма пары чисел
    seven = to_7th(pair_sum)          # Перевод суммы в семеричную с/с (строка)
    # Если полиндром, добавить в список
    if seven == seven[::-1]:
        sums.append(int(seven))

# Вывод количества сумм и максимальной суммы
print(len(sums), max(sums))

