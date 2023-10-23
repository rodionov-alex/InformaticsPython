# Если маска подсети 255.255.240.0 и IP-адрес компьютера в сети 232.126.150.18, то номер компьютера в сети равен_____
#
# Ответ: 1554

ip = [bin(int(x))[2:].zfill(8) for x in '232.126.150.18'.split('.')]
mask = [bin(int(x))[2:].zfill(8) for x in '255.255.240.0'.split('.')]

print(*ip)
print(*mask)

print(int('011000010010', 2))
