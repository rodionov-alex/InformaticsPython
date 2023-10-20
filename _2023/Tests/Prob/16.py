# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = n при n ≥ 2025;
# F(n) = n +3 + F(n + 3), если n < 2025.
# Чему равно значение выражения F(2018) – F(2022)?
#
# Ответ: 4049

mx = 2030
f = [0] * mx

for n in range(mx - 1, -1, -1):
    if n >= 2025:
        f[n] = n
    else:
        f[n] = n + 3 + f[n + 3]

print(f[2018] - f[2022])
