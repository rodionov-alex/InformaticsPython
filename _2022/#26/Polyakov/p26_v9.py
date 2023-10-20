with open('26_9.txt') as f:
    nums = list(map(int, f.readlines()[1:]))
    t = len(nums)
    nums.sort()
    minsr = max(nums)
    k = 0
    min_sr = nums[t // 2 - 1]
    max_sr = nums[3 * t // 4]

    for i in range(t - 1):
        for j in range(i + 1, t):
            s = nums[i] + nums[j]
            if s % 2 == 0:
                sr = s // 2
                if min_sr < sr < max_sr:
                    k += 1
                    minsr = min(sr, minsr)
    print(k, minsr)