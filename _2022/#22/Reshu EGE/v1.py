t = 0
for i in range(1000):
    x = i
    L = 0
    M = 0

    while x > 0 :
        L = L+1
        if (x % 2) != 0:
            M = M + x % 8
        x = x // 8

    if L == 3 and M == 6 and i > t:
        t = i

print(t)
print(L)
print(M)