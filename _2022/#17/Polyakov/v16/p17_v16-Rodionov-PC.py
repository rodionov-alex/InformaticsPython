def has_2_at_0_raz_in_3_ss(num):
    return num % 3 == 2

f = open('16.txt')
lines = f.readlines()
f.close()

nums = [int(i) for i in lines]
has_2 = []

for i in range(len(nums)):
    if has_2_at_0_raz_in_3_ss(nums[i]):
        has_2.append(i)

cnt = 0

for i in has_2:
    if i == 0 or i == len(nums) - 1:
        cnt += 1
    elif i == 1 or i == len(nums) - 2:
        cnt += 2
    else:
        cnt += 3

#print(len(has_2), has_2)
print(cnt)

cnt = 0

if has_2_at_0_raz_in_3_ss(nums[0]):
    cnt += 1
if has_2_at_0_raz_in_3_ss(nums[len(nums) - 1]):
    cnt += 1
if has_2_at_0_raz_in_3_ss(nums[1]):
    cnt += 2
if has_2_at_0_raz_in_3_ss(nums[len(nums) - 2]):
    cnt += 2

for i in range(2, len(nums) - 2):
    if has_2_at_0_raz_in_3_ss(nums[i]):
        cnt += 3

print(cnt)