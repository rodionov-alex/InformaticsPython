with open('17.txt') as f:
    data = list(map(int, f))
    mx3 = max([x for x in data if 100 <= abs(x) <= 999]) ** 3
    sdata = [sum(map(int, str(abs(x)))) for x in data]
    res = []

    for i in range(1, len(data)):
        if (sdata[i] % 5 == 0 and sdata[i - 1] % 5 or sdata[i - 1] % 5 == 0 and sdata[i] % 5) and \
           abs(data[i] ** 2 - data[i - 1] ** 2) >= mx3:
            res.append(data[i] + data[i - 1])

    print(len(res), max(res), sep='\t')
