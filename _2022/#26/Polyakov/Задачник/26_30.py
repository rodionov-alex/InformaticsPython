f = open(r'26data/26-J5.txt').readlines()
nums = [int(x) for x in f[1:]]
ln = len(nums)
nums0 = [nums[0]]
for i in range(1, ln - 1):
    x1 = nums[i - 1]
    x2 = nums[i]
    x3 = nums[i + 1]
    m = [x1, x2, x3]
    m.sort()
    med = m[1]
    nums0.append(med)

nums0.append(nums[ln - 1])

ras = 0
for i in range(ln):
    r = nums[i] - nums0[i]
    if r > 0:
        ras += r
minn = min(nums0)
print(nums0.count(minn))
print(ras)
print(sum(nums) - sum(nums0))