from collections import defaultdict

with open('26.txt') as f:
    n = int(f.readline())

    gryadka_dic = {}

    for i in range(n):
        t = tuple(map(int, f.readline().split()))
        if t[0] in gryadka_dic:
            gryadka_dic[t[0]].append(t[1])
            gryadka_dic[t[0]].sort()
        else:
            gryadka_dic[t[0]] = [t[1]]

    gryadka = []

    for row in gryadka_dic:
        gryadka.append((row, gryadka_dic[row]))

    gryadka.sort(reverse=True)

    res_row = 0
    res_pos = 0

    for row in gryadka:
        if len(row[1]) > 1:
            for i in range(len(row[1]) - 1):
                if row[1][i + 1] - row[1][i] == 12:
                    res_row = row[0]
                    res_pos = row[1][i] + 1
                    break

        if res_row != 0:
            break

    print(res_row, res_pos)

