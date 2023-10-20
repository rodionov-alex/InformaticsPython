r = 9999999

for i in range(100000):
    a = 0
    b = 0
    x = i
    t = 0

    while x > 0:
        y = x % 10

        if y > 3:
            a = a+1

        if y < 8:
            b = b+1

        x = x // 10
        t += 1

    if (a == 4 and b == 2 and i < r and t == 5):
        r = i
        break

print(r)