f = open('27-B.txt')
n = int(f.readline())

sm = 0
ras = []

for i in range(n):
    line = f.readline()
    pair = [int(k) for k in line.replace('  ', ' ').split(' ')]
    mx = max(pair)
    sm += mx
    r = mx - min(pair)

    if r % 3 != 0:
        ras.append(r)

if sm % 3 == 0:
    sm -= min(ras)

print(sm)
