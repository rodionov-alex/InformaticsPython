def to_9(n):
    s = ''
    while n:
        s = str(n % 9) + s
        n //= 9
    return s

res = []

for i in range(int('10000', 9), int('88888', 9)):
    i9 = to_9(i)

    if i9.count('0') == 1:
        ind = i9.index('0')

        if int(i9[ind - 1]) % 2 == 0 and (ind == len(i9) - 1 or int(i9[ind + 1]) % 2 == 0):
            res.append(i9)

print(len(res))

