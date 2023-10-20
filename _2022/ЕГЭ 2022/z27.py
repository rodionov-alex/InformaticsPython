with open('z27_a.txt') as f:
    n = int(f.readline())
    bags = []

    for i in range(n):
        probes = int(f.readline())

        if probes % 38:
            bags.append(probes // 38 + 1)
        else:
            bags.append(probes // 38)

    total = len(bags)
    res = []

    for i in range(total):
        cost = 0

        for j in range(total):
            if i == j:
                continue
            dist = abs(i - j)
            cost += dist * bags[j]

        res.append(cost)
        res.sort(reverse=True)

    print(min(res), res.index(min(res)))