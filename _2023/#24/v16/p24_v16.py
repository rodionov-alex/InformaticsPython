# Текстовый файл 24-213.txt содержит строку из символов N, O и P, всего не более чем из 10^6 символов. Определите
# максимальное количество идущих подряд последовательностей символов NРО или РNО в прилагаемом файле. Искомая
# подпоследовательность должна состоять только из троек NРО или только из троек РNО или только из троек NРО и РNО
# в произвольном порядке их следования.
#
# Ответ: 297

with open('24-213.txt') as f:
    s = f.readline().strip().replace('NPO', '*').replace('PNO', '*')
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