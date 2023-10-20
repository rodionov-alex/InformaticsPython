with open('26_8.txt') as f:
    nums = list(map(int, f.readlines()[1:]))
    nums.sort()
    maxs = 0
    k = 0
    t = len(nums)
    print(t)
    for i in range(t - 101):
        for j in range(i + 101, t):
            s = nums[i] + nums[j]
            if s % 2 == 0:
                k += 1
                maxs = max(s, maxs)
    print(k, maxs // 2)
