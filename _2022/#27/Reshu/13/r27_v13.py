f = open('27_13_B.txt')
nums = list(map(int, f.readlines()[1:]))
f.close()

nums.sort(reverse=True)
ln = len(nums)

max_14 = 0
max_72 = 0
imax_14 = -1
imax_7 = -1
imax_2 = -1
i = 0

while (imax_14 < 0 or imax_7 < 0 or imax_2 < 0) and i < ln:
    if imax_14 < 0 and nums[i] % 14 == 0:
        imax_14 = i
    elif imax_7 < 0 and nums[i] % 14 and nums[i] % 7 == 0:
        imax_7 = i
    elif imax_2 < 0 and nums[i] % 14 and nums[i] % 2 == 0:
        imax_2 = i

    i += 1

if imax_14 >= 0:
    if imax_14 == 0:
        max_14 = nums[imax_14] * nums[1]
    else:
        max_14 = nums[imax_14] * nums[0]

if imax_7 >= 0 and imax_2 >= 0:
    max_72 = nums[imax_7] * nums[imax_2]

print(max(max_14, max_72))
