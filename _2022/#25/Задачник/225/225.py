from tqdm import tqdm


def ch_d_count(num):
    z = 0
    sqrt = int(num ** 0.5)
    d = 0
    while d <= sqrt:
        d += 1
        if num % d == 0:

            if d % 2 == 0:
                z += 1

            d2 = (num // d)

            if d != d2 and d2 % 2 == 0:
                z += 1
    return z

count = 5
k = 0

for k in tqdm(range(22000, 510000, 2)):
    nk = 1850000000 + k

    w = ch_d_count(nk)

    if w % 2:
        print(k, w)
        count -= 1

    if count == 0:
        break

