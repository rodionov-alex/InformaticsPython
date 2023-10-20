with open('17.txt') as f:
    nums = list(map(int, f.readlines()))
    n17 = 0

    for n in sorted(nums):
        if n % 17 == 0:
            n17 = n
            break

    count = 0
    ln = len(nums)
    mx = 0

    for i in range(ln - 1):
        if nums[i] % n17 == 0 or nums[i + 1] % n17 == 0:
            count += 1
            mx = max(mx, nums[i] + nums[i + 1])

    print(n17, count, mx)

