def find_min_sum(nums_list: list):
    nums_list.sort()
    cnt = len(nums_list)
    res = []

    for i in range(cnt - 2):
        for j in range(i + 1, cnt - 1):
            for k in range(j + 1, cnt):
                sm = nums_list[i] + nums_list[k] + nums_list[j]

                if sm % 3 == 0:
                    return sm
    return 0


f = open('27-B.txt')
nums = [int(i) for i in f.readlines()[1:]]
f.close()
print(find_min_sum(nums))

