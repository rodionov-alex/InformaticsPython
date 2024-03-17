f = [1] * 2030

for n in range(2023, 0, -1):
    f[n] = f[n + 2] + f[n + 4]

print(len(set(f)))
