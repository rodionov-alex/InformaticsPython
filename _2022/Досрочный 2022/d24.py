with open('24.txt') as f:
    s = f.readline()
    s = s.replace('AC', '1').replace('AB', '1')

    count = 0
    mx = 0

    for c in s:
        if c == '1':
            count += 1
            mx = max(mx, count)
        else:
            count = 0

print(mx)

