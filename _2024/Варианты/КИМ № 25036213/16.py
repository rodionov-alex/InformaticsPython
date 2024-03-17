from functools import lru_cache

# Вариант 1
@lru_cache(None)
def f(n):
    if n <= 5:
        return n
    else:
        return 2 * n - 8 + f(n - 2) + f(n - 1) // 8

print(f(163))

# Вариант 2
f = [0] * 164

for n in range(164):
    if n <= 5:
        f[n] = n
    else:
        f[n] = 2 * n - 8 + f[n - 2] + f[n - 1] // 8

print(f[163])
