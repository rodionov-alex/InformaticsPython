res = []

for n in range(4, 1000):
    bn = bin(n)[2:]

    if n % 3 == 0:
        r = int(bn + bn[-3:], 2)
    else:
        r = int(bn + bin((n % 3) * 3)[2:], 2)

    if r > 151:
        res.append(r)

print(min(res))

# Ответ: 163
