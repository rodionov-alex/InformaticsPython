def d(n, m):
    return n % m == 0


a = 1

while True:
    for x in range(1, 100000):
        f = (d(x, 3) <= (not d(x, 5))) or (x + a >= 70)
        if f == 0:
            break
    else:
        print(a)
        break

    a += 1
