n = 0
r = 0
while r <= 97:
    n += 1
    bn = bin(n)[2:]

    if n % 2 == 0:
        bn += '01'
    else:
        bn += '10'

    r = int(bn, 2)

print(n)