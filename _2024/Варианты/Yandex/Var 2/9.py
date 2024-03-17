with open('9.txt') as f:
    data = [tuple(map(float, x.replace(',', '.').split())) for x in f]
    print(data)
    count = 0

    for t, to, wind in data:
        if t - to >= 5 and (0 <= wind <= 45 or 315 <= wind <= 360):
            count += 1

    print(count)