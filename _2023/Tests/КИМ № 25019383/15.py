def d(n, m):
    return n % m == 0

B = [x for x in range(50, 71)]

def f(x, A):
    return d(x, A) or (d(x, 23) <= (x not in B))

for A in range(1, 1000000):
    for x in range(1, 1000):
        if f(x, A) == 0:
            break
    else:
        print(A)
