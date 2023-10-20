# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n. Так, например, 14 & 5 =
# = 11102 & 01012 = 01002 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
# ((x & 52 ≠ 0) /\ (x & 36 = 0)) → ¬ (x & А = 0)
# тождественно истинна (т.е. принимает значение 1) при любом неотрицательном целом значении переменной х?
#
# Ответ: 16

def f(x, a):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & a == 0))

for a in range(1000000):
    for x in range(1000):
        if f(x, a) == 0:
            break
    else:
        print(a)
        break