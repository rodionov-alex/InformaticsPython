def getDivs(num):
    divs = set()

    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            divs.add(d)
            divs.add(n // d)

    return sorted(divs)


count = 5
n = 650_000
res = []

while count:
    n += 1
    divs = getDivs(n)
    k = (divs[0] + divs[-1]) if len(divs) else 0

    if len(divs) == 6 and 1000 <= k <= 9999:
        res.append((n, k))
        count -= 1

for n, k in sorted(res, reverse=True):
    print(n, k, sep='\t')
