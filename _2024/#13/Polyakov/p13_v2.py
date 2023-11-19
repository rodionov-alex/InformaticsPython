"""
В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла
сети относится к адресу сети, а какая - к адресу узла в этой сети. Адрес сети получается в результате применения
поразрядной конъюнкции к заданному адресу узла и маске сети. Сеть задана IP-адресом 216.130.64.0 и маской сети
255.255.192.0. Сколько в этой сети IP-адресов, которые не имеют ни одного байта с нечётным значением? IP-адрес
сети учитывать не следует.

Ответ: 4095
"""

ip = tuple(bin(x)[2:].zfill(8) for x in (216, 130, 64, 0))
mask = tuple(bin(x)[2:].zfill(8) for x in (255, 255, 192, 0))
print(*ip)
print(*mask)

# Первый и второй байты фиксированные и четные.
# В третьем байте 2 бита фиксированные и 6 нет. Поэтомиу количество возможных значений второго байта равно 2^6 = 64.
# Итого из них половина четные и половина нечетные: 32.
# В четвертом байте все биты свободные, а значит из 256 чисел - 128 четных.
# Итого 32 * 128 - 1 (IP-адрес сети учитывать не следует).

print(32 * 128 - 1)
