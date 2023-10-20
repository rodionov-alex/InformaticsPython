nMin = 2000000
nMax = 3000000

for n in range(nMin, nMax + 1):
    rBound = int(n ** 0.5)
    count = 0

    for d in range(1, rBound + 1):
        if n % d == 0 and n // d - d <= 115:
            count += 1

    if count >= 3:
        print(n)
