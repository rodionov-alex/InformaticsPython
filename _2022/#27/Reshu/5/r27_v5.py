f = open('27-B.txt')
nums = [int(i) for i in f.readlines()[1:]]
f.close()

nums.sort(reverse=True)

max_14 = 0
max_7 = 0
max_2 = 0
mx = nums[0]

for n in nums:
    if n % 14 == 0 and n > max_14:
        max_14 = n

        if mx == max_14:
            mx = nums[1]

    if n % 7 == 0 and n % 2 != 0 and n > max_7:
        max_7 = n

    if n % 2 == 0 and n % 7 != 0 and n > max_2:
        max_2 = n

print(max(max_14 * mx, max_7 * max_2))