def f(x, y, a):
    return (x + 2 * y < a) or (y > x) or (x > 60)

a = -1

while True:
    a += 1

    for x in range(100):
        for y in range(100):
            if f(x, y, a) == 0:
                break
        else:
            continue

        break
    else:
        print(a)
        break



# Ответ: 181
