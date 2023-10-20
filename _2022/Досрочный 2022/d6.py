i = 0
n = 0

while n != 8:
    i += 1
    s = i
    s = (s - 10) // 7
    n = 1

    while s > 0:
        n *= 2
        s -= n

print(i)