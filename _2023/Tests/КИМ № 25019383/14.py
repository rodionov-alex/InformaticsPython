for x in range(16):
    n1 = 17 ** 3 + x * 17
    n2 = 15 * 17 ** 4 + x * 17 ** 2 + 15 * 17 + 15
    r = n1 + n2
    if r % 13 == 0:
        print(r // 13)
        break