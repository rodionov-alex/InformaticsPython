"""
Текстовый файл 24-263.txt состоит не более чем из 10^6 символов и содержит только заглавные буквы латинского
алфавита. Определите максимальную длину подстроки, в которой символ Y встречается не более 150 раз.

Ответ: 5195
"""

with open('Files/24-263.txt') as f:
    s = f.readline().strip()
    length = 0
    max_length = 0
    count_y = 0
    sbegin = 0

    for i in range(len(s)):
        length += 1

        if s[i] == 'Y':
            count_y += 1

        if count_y > 150:
            max_length = max(max_length, length - 1)

            while count_y > 150:
                if s[sbegin] == 'Y':
                    count_y -= 1

                length -= 1
                sbegin += 1

    max_length = max(max_length, length)
    print(max_length)
