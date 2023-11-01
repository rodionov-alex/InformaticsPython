import string
f = open(r'F:\Informatics\Python\Mine\#24\v1\24.txt')

lineNumb = -1
counts = []

nCount = 999999
ln = ''
numb = 0

for line in f:
    lineNumb += 1
    nCnt = line.count('N')
    counts.append(nCnt)

    if nCnt > 0 and nCnt < nCount:
        nCount = nCnt
        ln = line
        numb = lineNumb


f.close()

cCount = 0
res = ''

for c in string.ascii_uppercase:
    cnt = ln.count(c)

    if cnt >= cCount:
        cCount = cnt
        res = c

print(res)