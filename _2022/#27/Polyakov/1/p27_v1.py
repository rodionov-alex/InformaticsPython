def is_good(numb):
    return (numb % 5 == 0 and numb % 7 != 0) or (numb % 5 != 0 and numb % 7 == 0)

#def gcd(a, b):
#    while b > 0:
#        temp = b
#        b = a % b
#        a = temp
#    return a

#def lcm(a, b):
#    return (a * b) // gcd(a, b)

with open('27_1b.txt') as f:
    n = int(f.readline())

    list_of_lcm = []

    for i in range(n):
        list_of_lcm.append([])

    for r in range(n):
        nums = list(map(int, f.readline().split()[1:]))
        cnt = len(nums)

        for i in range(cnt - 1):
            for j in range(i + 1, cnt):
                x = nums[i]
                y = nums[j]
                ij_lcm = lcm(x, y)
                list_of_lcm[r].append(ij_lcm)

max_sum = 0

for lcms in list_of_lcm:
    lcms.sort(reverse=True)
    max_sum += lcms[0]

if not is_good(max_sum):
    diffs = []

    for x in list_of_lcm:
        for i in range(1, len(x)):
            diffs.append(x[0] - x[i])

    diffs.sort()

    for x in diffs:
        if is_good(max_sum - x):
            max_sum -= x
            break

print(max_sum)