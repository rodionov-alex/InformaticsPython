f = open('24_6.txt')
lines = f.readlines()
f.close()

chains = []

#перебор строк
for line in lines:
    sLen = len(line)

    #в строке должно быть меньше 30 букв R
    if line.count('R') >= 30:
        continue

    #посимвольный перебор
    for i in range(sLen - 1):
        j = i + 1
        chainLen = 1

        while line[i] != line[j]:
            chainLen += 1
            j += 1

            #если дошли до конца строки - прерываем
            if j == sLen:
                chainLen = 1
                break

        if chainLen >= 3:
            chains.append(chainLen)

        chainLen = 1

print(max(chains), len(chains))





