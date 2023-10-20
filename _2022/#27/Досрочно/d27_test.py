with open('test.txt') as f:
    nums = list(map(int, f.readlines()[1:]))
    n = len(nums)
    half = n // 2
    wide_nums = (nums * 3)[half:3*n-half]
    mult = []
    costs = []

    for j in range(half):
        mult.append(j)
    for j in range(half, 0, -1):
        mult.append(j)

    prices = []

    for i in range(n):
        prices.append(nums[i] * mult[i])

    #print(nums)
    #print(mult)
    #print(prices)
    #print(wide_nums)

    total_cost = sum(prices)
    costs.append(total_cost)

    for i in range(1, n):
        j = i + half
        total_cost += sum(wide_nums[j - half:j]) - sum(wide_nums[j:j + half])
        costs.append(total_cost)

    print(costs)
    print(costs.index(min(costs)) + 1)




