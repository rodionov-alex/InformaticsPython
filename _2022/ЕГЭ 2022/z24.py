import itertools

gl = 'AO'
sg = 'DCF'

iter = list(itertools.product(sg, gl))

combs = []

for x in iter:
    combs.append(''.join(x))

with open('z24_text.txt') as f:
    s = f.readline().strip()
    k = 0
    maxk = 0

    i = 0
    length = len(s)

    while i < length - 1:
        sr = s[i:i + 2]
        if sr in combs:
            k += 1
            i += 1
        else:
            maxk = max(maxk, k)
            k = 0
        i += 1
print(maxk)
print(combs)