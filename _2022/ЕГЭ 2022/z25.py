mask = '123{0}67'

res = []

for i in range(1, 4):
    for j in range(10 ** i):
        num = str(j)

        while len(num) < i:
            num = '0' + num

        n = int(mask.format(num))

        if n % 123 == 0:
            res.append(n)

for x in sorted(res):
    print(x, x // 123)