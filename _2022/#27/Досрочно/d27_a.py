from tqdm import tqdm

f = open('27-A.txt').readlines()
nums = [int(x) for x in f[1:]]
ln = len(nums)
half = ln // 2
sums = []
for i in tqdm(range(ln)):
    part1 = []
    part2 = []
    ind = i

    while len(part1) < half:
        part1.append(nums[ind])
        ind += 1

        if ind >= ln:
            ind = 0

    while len(part2) < half:
        part2.append(nums[ind])
        ind += 1

        if ind >= ln:
            ind = 0

    summ = 0

    for j in range(half):
        summ += part1[j] * j

    for j in range(half):
        summ += part2[j] * (half - j)

    sums.append((i + 1, summ))

print(min(sums, key=lambda x: x[1]))

