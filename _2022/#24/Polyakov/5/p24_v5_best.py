with open("24_5.txt") as f:
    s = f.readline()
    k = s.count("KEGE")  # Кол-во вхождений "KEGE"

print("Кол-во вхождений KEGE = ", k)
posM = []  # Массив номеров позиций вхождений "KEGE"
start = 0  # Начальная позиция поиска

for i in range(0, k):
    n = s.find("KEGE", start)  # Поиск позиции
    posM.append(n)
    start = n + 1              # Сдвиг позиции поиска

maxK = posM[2] + 3  # Длина цепочки до вхождения №3

for i in range(3, k):
    n = (posM[i] + 3) - (posM[i - 3] + 1)  # Длина цепочки между [i] и [i-3]

    if n > maxK:
        maxK = n

kL = len(s)                 # Длина всей строки
n = kL - (posM[k - 3] + 1)  # Длина последней цепочки

if n > maxK:
    maxK = n

print("Ответ: maxK=", maxK)
