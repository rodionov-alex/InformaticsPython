def f(a, x, y):
    return (3 * x + y > a) and (y < x) and (x < 30)

a = -1

while True:
    a += 1

    for x in range(500):
        for y in range(500):
            if f(a, x, y):
                break
        else:
            continue
        break
    else:
        print(a)
        break
