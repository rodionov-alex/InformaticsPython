f = open('24_2.txt')
s = f.readline().strip()
s = s + s
cur = mx = 1
st = s[0]
mst = ''

for i in range(1, len(s)):
    if s[i-1] <= s[i]:
        cur += 1
        st += s[i]

        if cur > mx:
            mx = cur
            mst = st
    else:
        cur = 1
        st = s[i]

print(mx, mst)
f.close()
