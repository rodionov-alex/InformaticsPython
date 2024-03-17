with open('27-B.txt') as f:
    data = list(map(int, f.readlines()[1:]))
    n = len(data)
    half = n // 2

    costs = [0] * n
    sum1, sum2 = 0, 0

    for i in range(1, half):
        costs[0] += data[i] * i + data[-i] * i
        sum1 += data[i]
        sum2 += data[-i]

    costs[0] += data[half] * half

    for i in range(1, n):
        costs[i] = costs[i - 1] - sum1 + sum2 - data[(i + half - 1) % n] + data[i - 1]
        sum1 = sum1 - data[i] + data[(i + half - 1) % n]
        sum2 = sum2 - data[(i + half) % n] + data[i - 1]

    print(costs.index(min(costs)) + 1)




