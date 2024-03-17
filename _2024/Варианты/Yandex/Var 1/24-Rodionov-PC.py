with open('24.txt') as f:
    s = f.readline().strip()
    glas = 'AEIOUY'
    gl_ind = 0 if s[0] in glas else -1
    cur_len = 1
    max_len = 0

    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            if s[i] in glas:
                max_len = max(max_len, cur_len)
                gl_ind = i
            else:
                cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 1

    max_len = max(max_len, cur_len)
    print(max_len)
