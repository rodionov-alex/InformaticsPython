from tqdm import tqdm

f = open('b.txt').readlines()[1:]
ras = []
s = 0

for i in tqdm(f):
    t = [int(x) for x in i.split(' ')]
    t.sort()
    s += t[2]
    r = t[2] - t[1]

    if r % 109 == 0:
        r = t[2] - t[0]

    if r % 109:
        ras.append(r)

m = min(ras)

if s % 109:
    print(s)
else:
    print(s - m)