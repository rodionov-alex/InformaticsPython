t = 700
for i in range(600,700):
    s = i
    n = 1
    while n < 21:
        s = s - 1
        n = n + 2
    if s == 601 and i < t:
        t = i
print(t)