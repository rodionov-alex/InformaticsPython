t = 1000

for i in range(t, 1, -1):
    s = i #s = int(input())
    n = 0
    while s < s*s:
        s = s - 1
        n = n + 3

    if n > 2000 and i < t:
        t = i
print(t)