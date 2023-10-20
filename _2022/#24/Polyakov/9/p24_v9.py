with open('24_9.txt') as f:
    lines = f.readlines()
    mx = 0

    for j in range(len(lines)):
        line = lines[j].strip()
        s = line.split('XYZ')  # Разобьем строку по XYZ, теперь каждый разрыв это XYZ
        c = 1

        for i in s:
            if i == '':  # Если нашли пустую подстроку, значит это место где стоят рядом два XYZ
                c += 1
            else:
                if c > mx:
                    mx = c
                c = 1

    print(mx * 3)  # Умножаем количество XYZ на 3 символа