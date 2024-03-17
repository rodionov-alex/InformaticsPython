def to4(num):
    res = ''

    while num:
        res = str(num % 4) + res
        num //= 4

    return res

res = ''

for n in range(199, 0, -1):
    if to4(n).endswith('123'):
        res += str(n)

print(res)
