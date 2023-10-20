f = open('27-A.txt')
n = int(f.readline())
lefts = []
for i in range(30):
    lefts.append(2 * 1000000000)

count = 0
sum = 0
maxsum = 0

for i in range(n):
    num = int(f.readline())
    sum += num
    if num % 2 == 1 and num > 0:
        count += 1
    d = count % 30

    if sum < lefts[d]:
        lefts[d] = sum

    maxsum = max(maxsum, sum - lefts[d])

print(maxsum)