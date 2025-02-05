f = open('24_6.txt')   # Открыть файл
lines = f.readlines()  # Считать все строки
f.close()              # Закрыть файл

chains = []  # Длины всех найденных цепочек

# Перебор строк
for line in lines:
    line_len = len(line)  # Длина строки

    # В строке должно быть меньше 30 букв R
    if line.count('R') < 30:
        # Посимвольный перебор от 0 до line_len - 1
        # (-1 нужна чтобы не выйти за границы строки при вычислении индекса следующего символа)
        for i in range(line_len - 1):
            chainLen = 1  # Длина цепочки

            # Поиск конца цепочки
            for j in range(i + 1, line_len):
                # Если найден конец цепочки
                if line[i] == line[j]:
                    # Минимальная длина цепочки = 3
                    if chainLen >= 3:
                        chains.append(chainLen)  # Добавить длину цепочки в список

                    break  # Прервать поиск конца цепочки
                # Если не найден - увеличить длину цепочки на 1
                else:
                    chainLen += 1

# Вывод самой длинной цепочки и количества цепочек
print(max(chains), len(chains))
