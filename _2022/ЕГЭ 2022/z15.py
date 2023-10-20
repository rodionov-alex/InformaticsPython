def d(m, n):
    return m % n == 0

A = 1

while True:
    for x in range(1, 10000):
        if not ((d(x, 3) <= (not d(x, 5))) or (x + A >= 90)):
            break
    else:
        print(A)
        break

    A += 1