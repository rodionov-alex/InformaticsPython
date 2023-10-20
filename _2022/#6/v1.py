f = 0
for i in range(150):
    s = i #s = int(input())
    n = 1
    while s < 208:
        s = s + 20
        n = n * 2

    if n == 256 and  i > f:
        f = i

print(f)