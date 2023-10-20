def has_0_in_16(num):
    return num % 16 == 0

f = open('17_17.txt')
lines = f.readlines()
f.close()

nums = list(map(int, lines))
has_0 = []

for i in range(len(nums)):
    if has_0_in_16(nums[i]):
        has_0.append(i)

cnt = 0
sm = 0

for i in range(len(has_0) - 1):
    r = has_0[i+1] - has_0[i]

    if r == 2:
        cnt += 1
        sm += max(nums[has_0[i]], nums[has_0[i] + 1], nums[has_0[i] + 2])
    elif r == 1 and has_0[i] == 0:
        cnt += 1
        sm += max(nums[has_0[i]], nums[has_0[i] + 1], nums[has_0[i] + 2])
    elif r == 1 and has_0[i + 1] == len(nums) - 1:
        cnt += 1
        sm += max(nums[has_0[i]], nums[has_0[i] + 1], nums[has_0[i] - 1])
    elif r == 1:
        cnt += 2
        sm += max(nums[has_0[i]], nums[has_0[i] + 1], nums[has_0[i] - 1])
        sm += max(nums[has_0[i]], nums[has_0[i] + 1], nums[has_0[i] + 2])

print(cnt, sm)

