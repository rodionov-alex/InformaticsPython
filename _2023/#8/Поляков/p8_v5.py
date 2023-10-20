# Михаил составляет 6-значные числа, которые кратны значению первой цифры 12-ричной системы записи этого числа.
# Сколько таких чисел он мог получить?
#
# Ответ: 477703

def to_12(number):
    res = ''

    while number != 0:
        ost = number % 12

        if ost == 10:
            ost = 'a'
        elif ost == 11:
            ost = 'b'
        else:
            ost = str(ost)

        res = ost + res
        number //= 12

    return res


count = 0

for num in range(100000, 1000000):
    n12 = to_12(num)
    n = int(n12[0], 12)

    if num % n == 0:
        count += 1

print(count)
