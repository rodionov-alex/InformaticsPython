f = open('b.txt')
n = int(f.readline())
summ = 0
nekr109 = 10000000000000
for i in range(n):
    a,b,c = f.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    summ += max(a, b, c)
    n1 = max(a, b, c) - min(a, b, c)
    sr = a+b+c-max(a, b, c) - min(a, b, c)
    n2 = max(a, b, c) - sr

    if n2%109 != 0:
        nekr109 = min(nekr109, n2)
    elif n1%109 != 0:
        nekr109 = min(nekr109, n1)

if summ%109!=0:
    print(summ)
else:
    print(summ-nekr109)