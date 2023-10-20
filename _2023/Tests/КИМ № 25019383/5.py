n = 1
r = 0

while r <= 249:
    n += 1
    bn = bin(n)[2:]
    b2n = bin(2 * n)[2:]
    b2n += str(bn.count('1') % 2)
    b2n += str(b2n.count('1') % 2)
    r = int(b2n, 2)

print(n)
