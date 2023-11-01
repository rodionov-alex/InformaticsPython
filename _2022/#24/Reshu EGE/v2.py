f = open('24.txt')

maxN = 0

for line in f:
    subStrings = line.split('XZZY')

    stringsCount = len(subStrings)

    for i in range(stringsCount):
        s = subStrings[i]
        n = len(s)

        # учет символов XZZ и ZZY (начало и конец XZZY)
        if i == 0 or i == stringsCount - 1:
            n += 3
        else:
            n += 6

        if n > maxN:
            maxN = n
            
print(maxN)
