with open('27_test.txt') as f:
    nums = list(map(int, f.readlines()[1:]))
    n = len(nums)
    half = n // 2

    costs = [0] * n
    sum1, sum2 = 0, 0

    for i in range(1, half):
        costs[0] += nums[i] * i + nums[-i] * i
        sum1 += nums[i]
        sum2 += nums[-i]

    costs[0] += nums[half] * half

    for i in range(1, n):
        costs[i] = costs[i - 1] - sum1 + sum2 - nums[(i + half - 1) % n] + nums[i - 1]
        sum1 = sum1 - nums[i] + nums[(i + half - 1) % n]
        sum2 = sum2 - nums[(i + half) % n] + nums[i - 1]

    print(costs.index(min(costs)) + 1)




