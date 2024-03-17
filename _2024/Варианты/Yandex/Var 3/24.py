with open('24.txt') as f:
    s = f.readline().strip().replace('C', ' ')
    strings = s.split()
    mx = 0

    for m in strings:
        while 'ABA' in m or 'BAB' in m:
            aba = m.find('ABA')
            bab = m.find('BAB')

            if aba < 0:
                m = m.replace('BAB', '*', 1)
            elif bab < 0:
                m = m.replace('ABA', '*', 1)
            else:
                m = m.replace('ABA' if aba < bab else 'BAB', '*', 1)

        lens = list(map(len, m.replace('A', ' ').replace('B', ' ').split()))

        if len(lens) > 0:
            mx = max(mx, max(lens))

    print(mx)
