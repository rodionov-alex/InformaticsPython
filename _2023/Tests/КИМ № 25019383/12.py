count = 0

for n in range(3, 51):
    s = '>' + '1' * n + '2' * n + '3' * n

    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>3', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>2', 1)

    s = s.replace('>', '')
    sm = sum([int(x) for x in s])

    if sm % 7 == 0:
        count += 1

print(count)
