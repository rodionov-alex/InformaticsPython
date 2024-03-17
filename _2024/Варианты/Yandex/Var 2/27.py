def f27a(file: str):
    with open(file) as f:
        n, tMax, kmPerDegree, tMin = tuple(map(int, f.readline().split()))
        # Сортированный по километражу список офисов
        offices = sorted([tuple(map(int, x.split())) for x in f])
        # Максимальное количество накормленных
        maxFed = 0
        # Перебор офисов, с которых начинается развоз
        for iStart in range(n):
            # Количество накормленных людей (изначально равно количеству стартового офиса)
            fed = offices[iStart][1]
            # Подсчет накормленных людей
            for i in range(iStart + 1, n):
                # Расстояние, пойденное до офиса
                distance = offices[i][0] - offices[iStart][0]
                # Температура еды
                tFood = tMax - distance // kmPerDegree
                # Если еда остыла - прекратить доставку
                if tFood <= tMin:
                    break
                # Еда не остыла - накормить
                else:
                    fed += offices[i][1]
            # Обновить максимум
            maxFed = max(maxFed, fed)

    return maxFed

def f27(file: str):
    with open(file) as f:
        n, tMax, kmPerDegree, tMin = tuple(map(int, f.readline().split()))
        # Максимальная дистанция перевозки еды
        maxDistance = (tMax - tMin) * kmPerDegree
        # Сортированный по километражу список офисов
        offices = sorted([tuple(map(int, x.split())) for x in f])
        # Начало и конец маршрута
        iStart = iEnd = 0
        # Количество накормленных людей (изначально равно количеству стартового офиса)
        fed = offices[iStart][1]
        # Пройденное расстояние
        distance = 0
        # Найдем количество накормленных при старте с самого первого офиса
        while distance <= maxDistance:
            iEnd += 1
            distance = offices[iEnd][0] - offices[iStart][0]
            # Если дистанция меньше максимальной, то добавить накормленных
            if distance <= maxDistance:
                fed += offices[iEnd][1]
            # Если нет, то сдвинем конечный индекс на 1 назад, после цикл будет закончен
            else:
                iEnd -= 1
        # Максимум накормленых человек
        maxFed = fed
        # Дальнейший перебор офисов использует количество накормленных предыдущих проверок
        while iStart < n - 1:
            # Сдвигаем индекс начала на 1 правее, так же уменьшим количество накормленных и расстояние
            fed -= offices[iStart][1]
            iStart += 1
            distance = offices[iEnd][0] - offices[iStart][0]
            # Пока позволяет максимальная дистанция - сдвигем правую границу
            while distance <= maxDistance and iEnd < n - 1:
                iEnd += 1
                distance = offices[iEnd][0] - offices[iStart][0]
                # Если дистанция меньше максимальной, то добавить накормленных
                if distance <= maxDistance:
                    fed += offices[iEnd][1]
                # Если нет, то сдвинем конечный индекс на 1 назад, после цикл будет закончен
                else:
                    iEnd -= 1
            # Обновить максимум
            maxFed = max(maxFed, fed)

    return maxFed

print(f27a('27_A.txt'))  # 374
print(f27('27_A.txt'))   # 374
print(f27('27_B.txt'))   # 125172
