nMin = 200000000
nMax = 400000000

power2 = []
power3 = []

p = 2
rp = 2 ** p

while rp < nMax:
    power2.append(rp)
    p += 2
    rp = 2 ** p

p = 1
rp = 3 ** p

while rp < nMax:
    power3.append(rp)
    p += 2
    rp = 3 ** p

res = []

for i in range(len(power2)):
    for j in range(len(power3)):
        r = power2[i] * power3[j]

        if r >= nMin and r <= nMax:
            res.append(r)

print(sorted(res))