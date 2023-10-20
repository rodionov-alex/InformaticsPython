n = 99
r = 1

while r % 4:
    n += 1
    bn = bin(n)[2:]

    for i in range(3):
        c0 = bn.count('0')
        c1 = bn.count('1')

        if c0 == c1:
            bn += bn[-1]
        elif c0 < c1:
            bn += '0'
        else:
            bn += '1'

    r = int(bn, 2)

print(n)
