f = open('test.txt')

k, s = 89, 0

mins = {0: (0, 0)}

res = []

for i in range(1, int(f.readline())+1):
    s += int(f.readline())

    if s % k in mins:
        res += [(s - mins[s % k][0], mins[s % k][1] - i)]
    else:
        mins[s % k] = (s, i)

print(-max(res)[1])
