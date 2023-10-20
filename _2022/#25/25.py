def primes(n) :
    res = {2}
    prime = [True] * (n+1)
    for i in range(3, n + 1, 2) :
        if not prime[i]:
            continue      #начинает следующий проход цикла, минуя оставшееся тело цикла
        res.add(i)
        for j in range(i * i, n+1, i):
            prime[j] = False
    return sorted(res)[1:][::-1]    #Сортировка
 
i = 912673
pr = primes(int(i**(1/3)))
res = []                              #Пустой список
for k in pr:
    for n in range(11, 2, -2):
        tmp = k**n
        if tmp < i:
            t = tmp // k
            s = t
            while t > k*k:
                t //= k
                s += t 
            if tmp % s == 0:
                res.append([tmp, s])  #Добавляем в список
 
#for elem in sorted(res):                   #Перебор всего списка
for elem in sorted(res, reverse=True)[:5]:  #Перебор 5 элементов списка в обр.порядке
    print(*elem)
