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

    gryadka.sort()

    res_row = 0
    mx = 0

    for row in gryadka:
        if len(row[1]) > 1:
            for i in range(len(row[1]) - 1):
                # Пример: 6 - 3 = 3, но между 6 и 3 всего 2, поэтому из разницы нужно дополнительно вычетать еще 1
                free_space = row[1][i + 1] - row[1][i] - 1
                if free_space >= mx:
                    mx = free_space
                    res_row = row[0]

    print(res_row, mx)

# 4802 7468

