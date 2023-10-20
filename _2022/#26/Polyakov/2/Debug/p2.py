import time

start = time.time()
f = open('26_2.txt').readlines()
O = f[0].split()
m = int(O[1])
f = f[1:]
sp = []
ans1 = 0
for i in f:
    sp.append(int(i))
while sum(sp) > m:
    sp.sort(reverse=True)
    s = 0
    n = -1
    while s < m:
        n += 1
        s += sp[n]
    ns = s - sp[n]
    ans1 += n
    sp = sp[n:]
    ost = m - ns
    for i in sp:
        if i < ost:
            break
        posl = i
    sp.remove(posl)
    sp.append(posl-ost)
count0 = sp.count(0)
ans2 = len(sp) - count0
print(ans1, ans2)

end = time.time()
total = end - start
print("%.3f" % total, "sec.")