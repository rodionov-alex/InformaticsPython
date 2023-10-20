t = 1000

for i in range(t, 1, -1):
    s = i #s = int(input())
    n = 50
    while s > 0:
        s = s // 2
        n = n - 3

    if n == 23 and i < t:
        t = i
print(t)