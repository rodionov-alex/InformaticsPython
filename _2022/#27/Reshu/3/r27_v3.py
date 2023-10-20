f = open('27-A.txt')
nums = [int(i) for i in f.readlines()[1:]]
f.close()

sums = []
sm = 0
sm301 = 0
cnt = 0

for n in nums:
    if n > 0 and n % 2 == 1:
        cnt += 1

    if cnt == 30 and not (n > 0 and n % 2 == 1):
        sm301 += n

    if cnt == 31:
        sums.append(sm)
        cnt = 1

    sm += n

mx = []
sm = 0

for s in sums:
    if s < 0 < sm:
        mx.append(sm)
    else:
        sm += s

if sm > 0:
    mx.append(sm)

print(max(mx))
