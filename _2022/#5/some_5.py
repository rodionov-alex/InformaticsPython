def to_9(num):
    res = ''

    while num:
        res = str(num % 9) + res
        num //= 9

    return res


for n in range(10000, 0, -1):
    n9 = to_9(n)

    for _ in range(5):
        if 0 < n9.count('5') == n9.count('7'):
            n9 += n9[-1]
        else:
            nums = dict()

            for ch in n9:
                if ch in nums:
                    nums[ch] += 1
                else:
                    nums[ch] = 1

            maxn = 0
            maxch = ''

            for ch in sorted(nums):
                if nums[ch] >= maxn:
                    maxn = nums[ch]
                    maxch = ch

            n9 += maxch

    n10 = int(n9, 9)

    if 'bac' in hex(n10):
        print(n)
        break