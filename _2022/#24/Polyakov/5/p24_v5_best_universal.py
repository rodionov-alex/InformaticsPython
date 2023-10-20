comb = "KEGE"  # Комбинация-разделитель звеньев цепочки
comb_max = 2   # Максимальное количество комбинаций в цепочке

f = open("24_5.txt")
s = f.readline()
f.close()
k = s.count(comb)  # Кол-во вхождений комбинации

print("Кол-во вхождений \'" + comb + "\' =", k)
posM = []  # Массив номеров позиций вхождений комбинации
start = 0  # Начальная позиция поиска

for i in range(0, k):
    n = s.find(comb, start)  # Поиск позиции
    posM.append(n)           # Добавить позицию в массив
    start = n + 1            # Сдвиг позиции поиска

maxK = posM[comb_max] + (len(comb) - 1)  # Длина цепочки до вхождения comb_max + 1

for i in range(comb_max + 1, k):
    # Длина цепочки между [i] и [i - (comb_max + 1)]
    n = (posM[i] + (len(comb) - 1)) - (posM[i - (comb_max + 1)] + 1)
    # Сравнение с максимальной
    if n > maxK:
        maxK = n

# Длина последней цепочки
n = len(s) - (posM[k - (comb_max + 1)] + 1)

if n > maxK:
    maxK = n

print("Ответ:", maxK)
