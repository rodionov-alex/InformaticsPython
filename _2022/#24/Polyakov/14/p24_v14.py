f = open(r"24.txt")
lines = f.readlines()
f.close()

maxChainResult = 0  # Максимальная длина цепочки

# Перебор строк
for line in lines:
    if line.count('G') < 15:
        sLen = len(line)

        # Посимвольный перебор
        for i in range(sLen - 1):
            j = i + 1        # Индекс правой границы цепочки
            maxChainLen = 0  # Максимальная длина цепочки в текущей строке
            chainLen = 1     # Длина цепочки

            # Анализ символов до конца строки
            while j != sLen:
                # Если найдены одинаковые символы - обновить текущую максимальную длину цепочки
                if line[i] == line[j]:
                    maxChainLen = chainLen

                # Инкремент
                chainLen += 1
                j += 1

            # Если длина текщей максимальной цепочки больше - обновить максимум
            if maxChainLen > maxChainResult:
                maxChainResult = maxChainLen

print(maxChainResult)
