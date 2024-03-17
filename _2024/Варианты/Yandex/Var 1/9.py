with open('9.txt') as f:
    data = [sorted(map(int, x.split())) for x in f]
    count = 0

    for d in data:
        if d[0] == d[1] and d[2] == d[3] and sum(d) == 360:
            count += 1

    print(count)
