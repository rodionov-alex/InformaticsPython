f = open('27_15_B.txt')
n = int(f.readline())

max1 = 0
max2 = 0
max3_1 = 0
max3_2 = 0

for i in range(n):
    num = int(f.readline())

    if num % 3 == 1:
        max1 = max(max1, num)
    elif num % 3 == 2:
        max2 = max(max2, num)
    elif num % 3 == 0:
        if num > max3_1:
            max3_2 = max3_1
            max3_1 = num
        elif num > max3_2:
            max3_2 = num

f.close()

print(max(max1 + max2, max3_1 + max3_2))
