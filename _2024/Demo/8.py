# Сколько существует восьмеричных пятизначных чисел, не содержащих
# в своей записи цифру 1, в которых все цифры различны и никакие две
# чётные или две нечётные цифры не стоят рядом?

from itertools import permutations

digits = '0234567'  # все цифры восьмеричной с/с, кроме 1 (по условию)
odd = '357'         # нечетные цифры
count = 0

def is_good(num):
    if num[0] != '0':
        # Меняем нечетные на 1, а четные на 2, и склеиваем в строку
        even_odd = ''.join(['1' if x in odd else '2' for x in num])
        # Никакие две четные или две нечетные цифры не стоят рядом
        return '22' not in even_odd and '11' not in even_odd

    return False

nums = [''.join(x) for x in permutations(digits, 5) if is_good(x)]

print(nums)
print(len(nums))

# Ответ: 180
