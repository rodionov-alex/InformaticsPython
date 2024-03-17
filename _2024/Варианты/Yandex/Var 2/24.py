from string import ascii_lowercase

# region Через замены
with (open('24.txt') as f):
    s = f.readline().strip().replace('3', 'e').replace('4', 'a')

    for ch in ascii_lowercase + '012567890':
        if ch not in 'yandex':
            s = s.replace(ch, ' ')

    s = s.replace('yandex', '*').replace('yande', '5 ').replace('yand', '4 ')
    s = s.replace('yan', '3 ').replace('ya', '2 ').replace('y', '1 ')

    for ch in 'andex':
        s = s.replace(ch, ' ')

    mx = 0

    for word in s.split():
        if '*' in word:
            mx = max(mx, word.count('*') * 6 + (int(word[-1]) if word[-1].isdigit() else 0))

    print(mx)
# endregion

# region Посимвольный перебор
with open('24.txt') as f:
    s = f.readline().strip()
    yand = ['y', 'a4', 'n', 'd', 'e3', 'x']
    yi = 0
    cur = 0
    mx = 0

    for ch in s:
        if ch in yand[yi]:
            cur += 1
            yi = yi + 1 if yi < 5 else 0
        else:
            mx = max(mx, cur)
            cur = 0
            yi = 0

    print(mx)
# endregion
