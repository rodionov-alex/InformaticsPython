f = open('27-8a.txt')
l = int(f.readline())
ras1 = []
ras2 = []
ras3 = []
ras4 = []
s1 = 0
s2 = 0
for i in range(l):
    x1, x2 = f.readline().split()
    x1, x2 = int(x1), int(x2)
    s1 += max(x1, x2)
    s2 += min(x1, x2)
    ras = abs(x1 - x2)
    if ras % 5 == 1:
        ras1.append(ras)
    elif ras % 5 == 2:
        ras2.append(ras)
    elif ras % 5 == 3:
        ras3.append(ras)
    elif ras % 5 == 4:
        ras4.append(ras)

ras1.sort()
ras2.sort()
ras3.sort()
ras4.sort()

ost = 5 - 2 * (s1 - s2) % 5
#if ost == 1:
print(ost)
print(ras1)
print(ras2)
print(ras3)
print(ras4)

print((s1 - s2))

