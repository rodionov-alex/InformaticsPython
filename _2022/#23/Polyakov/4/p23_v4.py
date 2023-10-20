def f(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return f(a + 3, b) + f(a * 3, b)


k = 0

for i in range(6, 99, 2):
    if f(3, i) > 0:
        k += 1

print(k)
