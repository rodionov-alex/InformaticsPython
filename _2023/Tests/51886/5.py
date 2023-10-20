def to_six(num):
    res = ''

    while num:
        res = str(num % 6) + res
        num //= 6

    return res

def f(n):
    n6 = to_six(n)
    n6 += n6[-1]
    bn = bin(int(n6, 6))[2:]
    bn += bn[-1]
    return int(bn, 2)

p = [f(x) for x in range(1, 1000)]

for m in range(343, 0, -1):
    if m in p:
        print(m)
        break
