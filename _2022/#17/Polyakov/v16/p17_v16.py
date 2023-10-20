def to_3(num):
    s = ''
    while num != 0:
        s = str(num % 3)
        num //= 3
    return s == '2'

f = open('17_16.txt')
lines = f.readlines()
f.close()

nums = [int(i) for i in lines]
has_2 = []

for i in range(len(nums)):
    if to_3(nums[i]):
        has_2.append(i)

cnt = 0

for i in has_2:
    if i == 0 or i == len(has_2) - 1:
        cnt += 1
    elif i == 1 or i == len(has_2) - 2:
        cnt += 2
    else:
        cnt += 3

print(has_2)
print(cnt)
