def prov(ch):
    for h in range(len(ch) - 1):
        if ch[h] >= ch[h + 1]:
            return False

    return True

otv = []

for i in range(6):
    for j in range(10 ** i):
        for k in range(10 ** (6 - i)):
            ch = '1' + str(j) + '5' + str(k) + '9'
            chi = int(ch)
            if prov(ch) and chi % 21 == 0:
                otv.append((chi, chi // 21))

for i in range(10 ** 6):
    chper = '1' + str(i) + '59'
    chposl = '15' + str(i) + '9'
    chperi = int(chper)
    if prov(chper) and chperi % 21 == 0:
        otv.append((chperi, chperi // 21))
    chposli = int(chposl)
    if prov(chposl) and chposli % 21 == 0:
        otv.append((chposli, chposli // 21))

pr = (0, 0)
otv.sort()
for i in otv:
    if pr != i:
        print(i)
    pr = i