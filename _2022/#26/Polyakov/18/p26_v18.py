f = open('26_18.txt')
lines = f.readlines()
f.close()

v_d, v_e, c = lines[0].split()
v_d = int(v_d)
v_e = int(v_e)

d = []
e = []

files = [int(i) for i in lines[1:]]

for i in files:
    if i > 500:
        d.append(i)
    else:
        e.append(i)
sd = sum(d)
se = sum(e)

d.sort(reverse=True)
e.sort(reverse=True)

while sd > v_d:
    sd -= d.pop(1)

while se > v_e:
    se -= e.pop(1)

#print(v_d, sum(d), max(d))
#print(v_e, sum(e), max(e))
print(len(d) + len(e), d[0] + e[0])