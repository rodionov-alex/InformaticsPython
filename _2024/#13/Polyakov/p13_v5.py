"""
В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса
узла сети относится к адресу сети, а какая - к адресу узла в этой сети. Адрес сети получается в результате
применения поразрядной конъюнкции к заданному адресу узла и маске сети. Некоторая сеть имеет маску 255.255.128.0.
Сколько в этой сети IP-адресов, для которых числовое значение четырёхбайтного IP-адреса кратно четырём?

Ответ: 8192
"""

mask = tuple(bin(x)[2:].zfill(8) for x in (255, 255, 128, 0))
print(*mask)

# Число кратно 4 если две его последние цифры равны нули или образуют число кратное 4. Таким образом нам важно
# значение только поcледнего четвертого байта ip-адреса. Посчитаем сколько таких чисел в интервале [0, 255].

count4 = 0

for x in range(256):
    if (x % 100) % 4 == 0:
        count4 += 1

# По скольку в третьем байте только 7 бит свободно - это 2 ^ 7 = 128 различных значений. Таким образом общее
# количество IP-адресов в этой сети, для которых числовое значение четырёхбайтного IP-адреса кратно четырём,
# равно произведению 128 * count4.

print(128 * count4)