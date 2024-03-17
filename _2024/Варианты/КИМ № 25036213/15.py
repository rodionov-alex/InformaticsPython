p1, p2, q1, q2 = 56, 79, 63, 85
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
A = []

def f(x):
    return (not ((x in P) <= (x in Q))) <= ((not (x in Q)) <= (x in A))

for x in [i / 10 for i in range(p1 * 10, q2 * 10 + 1)]:
    if not f(x):
        A.append(x)

print(A)
print(63-56)