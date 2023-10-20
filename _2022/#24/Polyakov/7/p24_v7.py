with open("24_7.txt") as f:
    s = f.readline()

    max_len = 5
    cur_len = 5

for i in range(len(s) - 5):
    if s[i:i + 3] != s[i + 3:i + 6]:
        cur_len += 1
        max_len = max(cur_len, max_len)
    else:
        cur_len = 5

print(max_len)
