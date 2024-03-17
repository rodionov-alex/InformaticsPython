ip = (192, 168, 32, 160)
mask = (255, 255, 255, 240)

bip = tuple(bin(x)[2:].zfill(8) for x in ip)
bmask = tuple(bin(x)[2:].zfill(8) for x in mask)

print(''.join(bip))
print(''.join(bmask))
print()

# По маске видим, что могут менться только последние 4 бита, а это 2^4 = 16 значений. Из них половина четных
# и половина нечетных. Поскольку в неизменяемой части четное количество единиц, то  и в изменяемой части тоже
# должно быть четное количество, а это 8 значений. Значит ответ 8. Далее программное решение.

count = 0
numbs = set()
# Инвертируем маску для поразрядной конъинкции
inverted_mask = tuple(int(''.join(['1' if y == '0' else '0' for y in x]), 2) for x in bmask)
# Запонение списка номеров сети
for ip4 in range(256):
    cur_ip = (192, 168, 32, ip4)
    numb = tuple(cur_ip[i] & inverted_mask[i] for i in range(4))
    numbs.add(numb)
# Подсчет количества с четным количеством единиц
for n in numbs:
    sip = '.'.join([bin(x)[2:].zfill(8) for x in n])

    if sip.count('1') % 2 == 0:
        count += 1

print(count)

# Ответ: 8
