n = 3
r = 0

while r <= 76:
    n += 1
    bn = bin(n)[2:]

    if n % 3 == 0:
        bn += bn[-3:]
    else:
        bn += bin(n % 3 * 3)[2:]

    r = int(bn, 2)

print(n)
