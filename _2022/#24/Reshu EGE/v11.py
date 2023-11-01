f = open(r'F:\Informatics\Python\Mine\#24\v18\24.txt')

maxN = 0
n = 0

e = 'XYZ'
le = len(e)
cur = 0

for line in f:
    for c in line:
        if c == e[cur]:
            cur += 1

            if cur == le:
                cur = 0
                n += 1
        else:
            if n > maxN:
                maxN = n
                
            n = 0
            cur = 0

print(maxN)