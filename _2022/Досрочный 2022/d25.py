res = []
num_format = '12345{0}6{1}8'


for i in range(10):
    for j in range(10):
        n = int(num_format.format(i, j))

        if n % 17 == 0:
            res.append((n, n // 17))

print(res)