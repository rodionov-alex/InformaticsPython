"""
Текстовый файл 24-264.txt состоит не более чем из 10^6 символов и содержит только заглавные буквы латинского алфавита
и цифры. Определите максимальную длину подстроки, которая может являться записью числа в шестнадцатеричной системе
счисления.

Ответ: 34
"""

from string import ascii_uppercase

def len16(n):
    while len(n) > 1 and n[0] == '0':
        n = n[1:]

    return len(n)

with open('Files/24-264.txt') as f:
    s = f.readline().strip()
    # Земеняем все буквы кроме ABCDEF на пробелы
    for x in ascii_uppercase[6:]:
        s = s.replace(x, ' ')

    print(max(list(map(len16, s.split()))))
