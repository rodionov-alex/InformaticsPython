res = []

for x in range(14):
    for y in range(14):
        n1 = 2 + x * 14 + 5 * 14 ** 2 + y * 14 ** 3 + 4 * 14 ** 4 + 1 * 14 ** 5
        n2 = 3 + y * 14 + 2 * 14 ** 2 + x * 14 ** 3 + 1 * 14 ** 4 + 3 * 14 ** 5
        r = n1 + n2
        if r % 9 == 0:
            res.append((x + y, x, y, r))

res.sort(reverse=True, key=lambda x: (x[0], x[1]))
res = res[0]

print(res[-1] // 9)
