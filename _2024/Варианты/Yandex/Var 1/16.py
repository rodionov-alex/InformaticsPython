f = [42] * 10010

for n in range(10000, 9993, -1):
    if n % 2:
        f[n] = -(n + f[n + 1] + f[n + 3])
    else:
        f[n] = 2 * n + f[n + 3] + f[n + 4] + f[n + 6]

print(f[9996] - f[9994])
