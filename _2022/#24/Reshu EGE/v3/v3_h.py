f = open(r'F:\Informatics\Python\Igor Lazu\#24\v3\test_24.txt').readlines()
l = len(f)
maxk = 0
for i in range(l):
    n = 0
    z = 0 # для прекращения цикла, если больше AB не нашлось
    while n == z:
        n += 1
        if 'AB'*n in f[i]:
            k = n*2
            z += 1
            if 'AB'*n+'A' in f[i]:
                k += 1
        if k > maxk:
            maxk = k
print(maxk)