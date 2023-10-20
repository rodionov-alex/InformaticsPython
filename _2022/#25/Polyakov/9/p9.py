def IsSimple(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    d = int(n ** 0.5)

    if d * d == n:
        return False

    for i in range(3, d, 2):
        if n % i == 0:
            return False

    return True
    
count = 4
n = 450000

while count > 0:
    n += 1
    dels = []
    rBound = int(n ** 0.5)

    if rBound * rBound == n and IsSimple(rBound):
        dels.append(rBound)

    for d in range(2, rBound):
        if n % d == 0:
            if IsSimple(d):
                dels.append(d)
            
            d2 = n // d

            if IsSimple(d2):
                dels.append(d2)

    m = 0
    
    if len(dels) > 0:
        m = max(dels) - min(dels)

    if m % 29 == 11:
        print(n, m, dels)
        count -= 1

print("END")