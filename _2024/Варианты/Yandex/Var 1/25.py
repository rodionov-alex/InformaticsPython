from fnmatch import fnmatch

res = []

for n in range(42, 2 * 10 ** 8, 42):
    sn = str(n)
    if fnmatch(sn, '1*7*') is False and fnmatch(sn, '?2*4*0'):
        res.append(n)

for i in range(-5, 0):
    print(res[i], res[i] // 42, sep='\t')
