n = 0
r = 0

while r <= 160:
    n += 1
    bn = bin(n)[2:]
    br = bn + bn[len(bn) - 1]

    if bn.count('1') % 2 == 0:
        br += '0'
    else:
        br += '1'

    if br.count('1') % 2 == 0:
        br += '0'
    else:
        br += '1'

    r = int(br, 2)

print(n)