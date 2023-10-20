count = 0

for n in range(1000, 10000):
    sn = str(n)
    n1 = int(sn[0])
    n2 = int(sn[1])
    n3 = int(sn[2])
    n4 = int(sn[3])

    arr = [n1 + n2, n2 + n3, n3 + n4]
    arr.remove(min(arr))
    arr.sort()
    r = int(''.join([str(x) for x in arr]))

    if r == 613:
        print(n)
        break



