with open('17.txt') as f:
    data = [int(x) for x in f]
    res = []

    for i in range(2, len(data) - 2):
        spair = sum(data[i:i + 2])

        if spair >= 0:
            _spair = sum(data[i - 2:i])

            if _spair >= 0:
                spair_ = sum(data[i + 2:i + 4])

                if 0 <= spair_ < spair and spair > _spair:
                    res.append(data[i] * data[i + 1])

    print(len(res), min(res))
