import re

res = []

for n in range(161, 17 * 10 ** 6 + 1, 161):
    if re.fullmatch(r'\d*1\d\d*\d68\d*', str(n)) is not None:
        res.append(n)

for i in range(0, len(res), 500):
    print(res[i], res[i] // 161)