f = open('17_19.txt')
lines = f.readlines()
f.close()

nums = [int(i) for i in lines]
sums = []

for i in range(len(nums) - 1):
    if nums[i] % 5 == 0 and nums[i+1] % 5 == 0:
        pair_sum = nums[i] + nums[i+1]
        sums.append(pair_sum)


print(len(sums), max(sums))