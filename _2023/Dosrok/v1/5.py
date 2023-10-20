for n in range(1000, 5, -1):
    bn = bin(n)[2:]
    if n % 3 == 0:
        bn += bn[-3:]
    else:
        bn += bin(3 * (n % 3))[2:]
    r = int(bn, 2)

    if r < 100:
        print(n)
        break