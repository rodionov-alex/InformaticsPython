# Текстовый файл 24-215.txt содержит строку из символов A, B, C и цифр 1, 2, 3, всего не более чем 106 символов.
# Определите максимальное количество идущих подряд троек символов вида «буква + цифра + буква».
#
# Ответ: 5

with open('24-215.txt') as f:
    s = f.readline().strip().replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1').replace('A1A', '*')
    mx = 0
    curLen = 0

    for i in s:
        if i == '*':
            curLen += 1
        else:
            mx = max(mx, curLen)
            curLen = 0

    mx = max(mx, curLen)

    s = s.replace('*1A', 'A1*')

    for i in range(n):
        if s[i] == '*':
            curLen += 1
        else:
            mx = max(mx, curLen)
            curLen = 0

    mx = max(mx, curLen)

    print(mx)
