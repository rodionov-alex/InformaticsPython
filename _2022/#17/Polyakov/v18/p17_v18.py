def has_111(num):
    return bin(num).count('1') == 3

f = open('17_18.txt')
lines = f.readlines()
f.close()

nums = [int(i) for i in lines]
indexes = []

for i in range(len(nums)):
    if has_111(nums[i]):
        indexes.append(i)

cnt = 0
sm = 0

for i in range(len(indexes) - 2):
    if indexes[i + 2] - indexes[i] == 2:
        cnt += 1
        sm += max(nums[indexes[i]], nums[indexes[i] + 1], nums[indexes[i] + 2])

print(cnt, sm)

