with open("24_3.txt") as f:      # Открыть файл
    line = f.readline().strip()  # Считать одну строку
    line_len = len(line)         # Длина строки
    maxlen = 0                   # Максимальная длина цепочки символов
    curlen = 1                   # Текущая длина цепочки символов

    # Посимвольный перебор строки от 0 до line_len - 1
    # (-1 нужна чтобы не выйти за границы строки при вычислении индекса следующего символа)
    for i in range(line_len - 1):
        # Если встретили сочетание 'PR' или 'RP', то цепочка прервалась
        sr = line[i:i + 2]
        if sr == 'PR' or sr == 'RP':
            # Сравнение длины текущей цепочки с максимальной
            if curlen > maxlen:
                maxlen = curlen

            curlen = 1  # Сброс текущей длины

        # Если сочетание не встретили, то увеличить длину текущей цепочки на 1
        else:
            curlen += 1  # Инкремент длины

    # Сравнение длины последней цепочки с максимальной
    if curlen > maxlen:
        maxlen = curlen

    # Вывод результата
    print(maxlen)
