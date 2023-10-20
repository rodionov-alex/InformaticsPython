# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = n!, если n ≥ 5000,
# F(n) = 2 * F(n + 1) / (n + 1), если 1 ≤ n < 5000.
# Чему равно значение выражения 1000 * F(7) / F(4)?
#
# Ответ: 26250

# Рассмотрим алгоритм под другим углом:
#
# f(5000) = 5000!
# f(n   ) = 2 * f(n + 1) / (n + 1)
# f(4999) = 2 * f(5000) / 5000 = 2 * 5000! / 5000 = 2 * 4999!
# f(4998) = 2 * f(4999) / 4999 = 2 * (2 * 4999!) / 4999 = 2 * 2 * 4998!
# f(4997) = 2 * f(4998) / 4998 = 2 * 2 * (2 * 4998!) / 4998 = 2 * 2 * 2 * 4997!
#
# Тут можно заметить закономерность, что каждое очередное f(n) вычисляется по формуле
# f(n) = 2 ^ (5000 - n) * n!
# Таким образом для чисел меньше 5000 можно использовть эту нерекурсивную функцию


import math as m


def f(n):
    return 2 ** (5000 - n) * m.factorial(n)


print(1000 * f(7) / f(4))
