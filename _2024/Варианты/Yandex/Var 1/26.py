with open('26.txt') as f:
    data = [tuple(map(int, x.split())) for x in f.readlines()[1:]]
    timeline = [0] * 1440

    for start, end in data:
        for i in range(start, end + 1):
            timeline[i] += 1

    res = []
    t = 0

    for m in timeline:
        if m == 0:
            t += 1
        else:
            if t > 0:
                res.append(t)
                t = 0

    if t > 0:
        res.append(t)

    print(len(res), sum(res))
