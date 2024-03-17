with open('Task/Доп_файлы/Задание 24/24_2024.txt') as f:
    s = f.readline().strip()
    length = 0
    max_length = 0
    count_t = 0
    sbegin = 0

    for i in range(len(s)):
        length += 1

        if s[i] == 'T':
            count_t += 1

        if count_t > 100:
            max_length = max(max_length, length - 1)

            while count_t > 100:
                if s[sbegin] == 'T':
                    count_t -= 1

                length -= 1
                sbegin += 1

    max_length = max(max_length, length)
    print(max_length)

# Ответ: 133

# with open('Task/Доп_файлы/Задание 24/24_2024.txt') as f:
#     s = f.readline()
#     m = 0
#     positions = [x for x in range(len(s)) if s[x] == 'T']
#
#     for i in range(len(positions) - 101):
#         m = max(positions[i + 101] - positions[i] - 1, m)
#
#     print(m)
