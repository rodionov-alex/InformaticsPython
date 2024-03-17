n = 0
r = 0

def to5(num):
    res = ''

    while num:
        res = str(num % 5) + res
        num //= 5

    return res

while r <= 10000:
    n += 1
    r5 = to5(n)

    if n % 25 == 0:
        r5 += r5[-3:]
    else:
        r5 += to5(n % 25)

    r = int(r5, 5)

print(n)
