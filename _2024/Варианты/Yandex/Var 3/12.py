N = 3
while True:
    N += 1

    if N >= 10000:
        print('fail')
        break

    for n in range(N, N + 1000):
        s = '8' + '4' * n

        while '4444' in s or '844' in s or '84' in s:
            if '4444' in s:
                s = s.replace('4444', '884', 1)
            if '844' in s:
                s = s.replace('844', '488', 1)
            if '84' in s:
                s = s.replace('84', '3343', 1)

        if len(s) < 20:
            break
    else:
        print(N)
        break
