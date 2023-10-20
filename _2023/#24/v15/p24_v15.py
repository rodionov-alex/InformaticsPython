# Текстовый файл 24-212.txt содержит строку из набора A, B, C, D, O, всего не более чем из 10^6 символов.
# Определите максимальное количество идущих подряд пар символов вида «гласная + согласная».
#
# Ответ: 202

with open('24-212.txt') as f:
    s = f.readline().strip().replace('O', 'A').replace('C', 'B').replace('D', 'B').replace('AB', '*')
    n = len(s)
    mx = 0
    curLen = 0

    for i in range(n):
        if s[i] == '*':
            curLen += 1
        else:
            mx = max(mx, curLen)
            curLen = 0

    mx = max(mx, curLen)

    print(mx)
