with open('17.txt') as f:
    data = [int(x) for x in f.readlines()]
    n_count = len(data)
    avg = sum(data) / n_count
    sums = []

    for i in range(n_count - 2):
        triple = data[i:i + 3]

        if any(tuple(x < avg for x in triple)) and \
           sum(tuple('9' in str(x) for x in triple)) == 3:
            sums.append(sum(triple))

    print(len(sums), max(sums))