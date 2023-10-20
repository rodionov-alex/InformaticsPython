with open('26-56.txt') as f:
    v, k, n = tuple(map(int, f.readline().split()))
    nums = list(map(int, f.readlines()))
    nums.sort()
    disks = [0] * k
    folder = []
    j = 0
    while len(nums):
        file = nums.pop()
        for i in range(j, len(disks)):
            if disks[i] + file <= v:
                disks[i] += file
                j = i + 1
                break
        else:
            folder.append(file)
            j = i + 1

        if j == k:
            j = 0

    print(disks)
    print(sum(folder), len(folder))

