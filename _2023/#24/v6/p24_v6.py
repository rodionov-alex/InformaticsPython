# Текстовый файл 24-223.txt содержит строку из символов A, B и C, всего не более чем 10^6 символов. Найдите
# максимальную длину строки, состоящей только из комбинаций AB и СAС. Например, в строке BABABCACABCB такая
# подстрока ABABCACAB (длина 9).
#
# Ответ: 69

with open('24-223.txt') as f:
    s = f.readline().strip().replace('AB', '*').replace('CAC', '#')
    n = len(s)
    mx = 0
    curLen = 0

    for i in range(n):
        if s[i] == '*':
            curLen += 2
        elif s[i] == '#':
            curLen += 3
        else:
            mx = max(mx, curLen)
            curLen = 0

    mx = max(mx, curLen)

    # Подводный камень:
    # Например строка CACACAB - обычная замена даст такой результат: #AC*. Получим, что подряд эти комбинации не идут.
    # Но если производить подмену не с первого вхождения подстроки CAC, а со второго, то результат будет совсем иным:
    # CACACAB => CA#*, и тут уже 2 комбинации будут стоять рядом, что в сумме даст нам более длинную комбинацию.

    s = s.replace('#AC', 'CA#')

    for i in range(n):
        if s[i] == '*':
            curLen += 2
        elif s[i] == '#':
            curLen += 3
        else:
            mx = max(mx, curLen)
            curLen = 0

    mx = max(mx, curLen)
    print(mx)
