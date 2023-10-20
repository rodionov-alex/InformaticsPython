nMin = 289123456
nMax = 389123456

for n in range(nMin, nMax + 1):
    rBound = int(n ** 0.5)
    dels = []

    if rBound * rBound == n:
        dels.append(rBound)

        for d in range(2, rBound):
            if n % d == 0:
                dels.append(d)
                dels.append(n // d)

        if len(dels) == 3:
            print(n, max(dels))