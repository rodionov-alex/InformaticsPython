# Текстовый файл 24-j5.txt состоит не более чем из 106 символов S, T, O, C, K.
# Определите максимальное количество подряд идущих комбинаций «KOT».

with open('24-j5.txt') as f:
    line = f.readline()
    line.strip()
    strs = line.split('KOT')

    mx = 0
    c = 1

    for s in strs:
        if s == '':
            c += 1
        else:
            mx = max(mx, c)
            c = 1

    print(mx)

# Ответ: 2