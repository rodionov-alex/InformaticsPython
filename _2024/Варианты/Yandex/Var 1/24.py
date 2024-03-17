"""
Текстовый файл состоит из заглавных букв латинского алфавита.

Определите последовательность наибольшей длины в прилагаемом файле, для которой выполняются два условия:

символы идут в алфавитном порядке,
в последовательности находится не более одной гласной (AEIOUY).
В ответе укажите длину найденной последовательности.

Пример:
Для строчки AEKZIOPSW ответ — число 4 (OPSW).
"""

with open('24.txt') as f:
    s = f.readline().strip()
    glas = 'AEIOUY'
    len_s = len(s)
    max_len = 0
    sbegin = 0
    gl_count = s[0] in glas

    for i in range(1, len_s):
        if s[i] >= s[i - 1]:
            if s[i] in glas:
                gl_count += 1

            if gl_count > 1:
                max_len = max(max_len, i - sbegin)

                while gl_count > 1:
                    if s[sbegin] in glas:
                        gl_count -= 1

                    sbegin += 1
        else:
            max_len = max(max_len, i - sbegin)
            gl_count = s[i] in glas
            sbegin = i

    max_len = max(max_len, len_s - sbegin)
    print(max_len)
