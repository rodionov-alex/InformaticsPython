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

    cost = 0
    cost_left = cost_right = 0

    # завод в 0
    for i in range(1, total):
        cost += bags[i] * i
        cost_right += bags[i]

    res.append(cost)

    # i перебирает заводы
    for i in range(1, total):
        cost_left = sum(bags[:i])
        cost = cost - cost_right + cost_left
        res.append(cost)
        cost_right = sum(bags[i+1:])

    print(min(res), res.index(min(res)))