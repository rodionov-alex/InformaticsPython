f = 500

for i in range(f, 0, -1):
    s = i #s = int(input())
    n = 0
    while s < 1000:
        s = s * 2
        n = n + 5

    if n == 10 and i < f:
        f = i
print(f)