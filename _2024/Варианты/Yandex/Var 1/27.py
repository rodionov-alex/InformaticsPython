def div(x):
    res = set()

    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            res.add(d)
            res.add(x // d)

    return sorted(res)

def f27(filename):
    with open(filename) as f:
        k = int(f.readline())
        n = int(f.readline())
        m = int(f.readline())
        a = [int(x) for x in f]

    count = 0

    # ПЕРЕБОР
    # for i in range(n):
    #     for j in range(i + k, n):
    #         for h in range(j + k, n):
    #             if a[i] * a[j] * a[h] % m == 0:
    #                 count += 1

    dv = div(m)
    d1, d2 = div(m)
    km = k1 = k2 = k0 = 0
    k2m = k21 = k22 = k20 = 0

    for i in range(2 * k, n):
        # Числа на расстоянии хотя бы 2k
        if a[i - 2 * k] % m == 0:
            km += 1
        elif a[i - 2 * k] % d1 == 0:
            k1 += 1
        elif a[i - 2 * k] % d2 == 0:
            k2 += 1
        else:
            k0 += 1

        # Пары на расстоянии хотя бы k
        if a[i - k] % m == 0:
            k2m += km + k2 + k1 + k0
        elif a[i - k] % d1 == 0:
            k2m += km + k2
            k21 += k1 + k0
        elif a[i - k] % d2 == 0:
            k2m += km + k1
            k22 += k2 + k0
        else:
            k2m += km
            k21 += k1
            k22 += k2
            k20 += k0

        # Тройки чисел
        if a[i] % m == 0:
            count += k2m + k21 + k22 + k20
        elif a[i] % d1 == 0:
            count += k2m + k22
        elif a[i] % d2 == 0:
            count += k2m + k21
        else:
            count += k2m

    return count


print(f27('test27.txt'))
print(f27('27_A.txt'))
print(f27('27_B.txt'))
