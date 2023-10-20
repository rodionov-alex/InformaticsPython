def issimple(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

k = 1
d2 = 2 ** k

while d2 <= 1048571 + 5:
    if d2 < 99999 - 5:
        k += 1
        d2 = 2 ** k
        continue

    for i in range(d2 - 5, d2 + 6):
        if 99999 <= i <= 1048571 and issimple(i):
            print(i, d2)

    k += 1
    d2 = 2 ** k

print('--')



