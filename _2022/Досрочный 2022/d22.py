k1, k2 = 0, 0
i = 0

while k1 != 10 or k2 != 19:
    i += 1

    s = i
    p = 10
    q = 8
    k1, k2 = 0, 0

    while s <= 100:
        s += p
        k1 += 1

    while s >= q:
        s -= q
        k2 += 1

    k1 += s
    k2 += s

print(i)