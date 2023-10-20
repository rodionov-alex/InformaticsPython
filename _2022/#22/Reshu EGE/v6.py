r = 9999
for k in range(1000):
    q = 0
    n = k
    for i in range(1, n):
        if n % i == 0:
            q = i
    
    if q == 17 and k < r:
        r = k

print(r)