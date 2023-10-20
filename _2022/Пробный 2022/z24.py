with open('24.txt') as f:
    s = f.readline().replace('BA', '1').replace('DA', '1')

    count = 0
    mx = 0

    for c in s:
        if c == '1':
            count += 1
            mx = max(mx, count)
        else:
            count = 0
print(mx)

# 151