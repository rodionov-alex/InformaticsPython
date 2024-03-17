with open('17.txt') as f:
    data = list(map(int, f))
    mn2 = sorted([x for x in data if 100 <= x <= 999])[1] ** 2
    res = []

    for i in range(len(data) - 1):
        sm = data[i] + data[i + 1]
        if sm < mn2:
            res.append(sm)

    print(len(res), max(res))
