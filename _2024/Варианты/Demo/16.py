f = [0] * 2026

for n in range(2025, 0, -1):
    if n > 2024:
        f[n] = n
    else:
        f[n] = n * f[n + 1]

print(f[2022] / f[2024])

# Ответ: 4090506
