f = open(r'F:\Informatics\Python\Mine\#24\v10\24.txt')

maxN = 0
n = 0

for line in f:
    for c in line:
        if c == 'C':
            n += 1
        else:
            if n > maxN:
                maxN = n
            n = 0

print(maxN)