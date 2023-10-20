with open('24-157.txt') as f:
    s = f.readline().strip()
    d = {}

    for i in range(len(s) - 2):
        sr = s[i:i + 3]

        if sr[0] == sr[2]:
            if sr[1] in d.keys():
                d[sr[1]] += 1
            else:
                d[sr[1]] = 1

    mk = ''
    mx = 0

    for k in d.keys():
        if d[k] > mx or (d[k] == mx and k < mk):
            mk = k
            mx = d[k]

    print(mk, mx, sep='')