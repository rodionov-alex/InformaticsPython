# Сколько существует восьмеричных пятизначных чисел, не содержащих
# в своей записи цифру 1, в которых все цифры различны и никакие две
# чётные или две нечётные цифры не стоят рядом?

from itertools import product

digits = '0234567'  # все цифры восьмеричной с/с кроме 1 (по условию)
nch = '357'         # нечетные цифры

def is_good(snum: str):
    if snum[0] != '0' and len(set(snum)) == 5:  # все цифры различны
        # Меняем четные на 0, а нечетные на 1
        chtncht = ''.join(['1' if x in nch else '0' for x in snum])
        # Никакие две четные или две нечетные цифры не стоят рядом
        return '00' not in chtncht and '11' not in chtncht

    return False

nums = [''.join(x) for x in product(digits, repeat=5) if is_good(''.join(x))]
print(len(nums))

# Ответ: 180
