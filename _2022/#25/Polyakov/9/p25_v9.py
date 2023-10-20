def is_simple(num):
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    sqrt_n = int(num ** 0.5)

    for i in range(3, sqrt_n + 1, 2):
        if num % i == 0:
            return False

    return True


count = 4
n = 450000

while count > 0:
    n += 1
    divs = []
    sqrt_d = int(n ** 0.5)

    for d in range(2, sqrt_d + 1):
        if n % d == 0:
            if is_simple(d):
                divs.append(d)
            d2 = n // d

            if d2 != d and is_simple(d2):
                divs.append(d2)

    m = 0
    if len(divs) > 0:
        m = max(divs) - min(divs)
    if m % 29 == 11:
        print(n, m)
        count -= 1
