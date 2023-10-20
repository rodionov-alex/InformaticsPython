def d(n, m):
    return n % m == 0

b1, b2 = 10, 40
b = [i / 10 for i in range(b1 * 10, b2 * 10 + 1)]

def f(x, a):
    return (x in a) or ((x in b) <= (not d(x, 6)))

a = set()

for x in [i / 10 for i in range(b1 * 10 - 1, b2 * 10 + 1)]:
    if f(x, a) == 0:
        a.add(x)

print(sorted(a), max(a) - min(a))
