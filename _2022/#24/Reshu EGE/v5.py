import string

f = open(r'F:\Informatics\Python\Mine\#24\v5\24.txt')
nMin = 9999999
nStr = ''
cMax = 0
char = ''


for line in f:
    nCnt = line.count('N')

    if nCnt < nMin:
        nMin = nCnt
        nStr = line

for c in string.ascii_uppercase:
    charCount = nStr.count(c)

    if charCount >= cMax:
        cMax = charCount
        char = c

print(char)