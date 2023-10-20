with open('24_8.txt') as f:
    lines = f.readlines()
    t = 'XYZX'
    mx = 0

    for line in lines:
        line = line.strip()
        c = 1

        for i in range(len(line)):
            if line[i:i + 2] in t:
                c += 1
            else:
                mx = max(c, mx)
                c = 1
                
        mx = max(c, mx)

    print(mx)