import time

def sumch(n):
    s = 0
    b = str(n)
    for i in b:
        s += int(i)
    return s

nmax = 50222022
nmin = 20222022

start_time = time.time()

a = []
for i in range(nmax + 1):
    a.append(i)
a[1] = 0
i = 2
while i <= nmax:
    if a[i] != 0:
        j = i + i
        while j <= nmax:
            a[j] = 0
            j = j + i
    i += 1
# Находим простые числа с помощью Решета Эратосфена меняя непростые числа на 0

lprst = [0]
kprst = 0
for i in a[2:]:
    if i:
        kprst += 1
    lprst.append(kprst)
# Создаём список где n-1 число обозначает количество простых чисел во факториале n числа

n = nmax
k = 5
while k:
    if sumch(n) % 22 == 0:
        prstfact = lprst[n - 1]
        if prstfact % 2022 == 0:
            print(n, prstfact)
            k -= 1
    n -= 1
# Единица не считается простым числом

print(time.time() - start_time)
# 134 секунды