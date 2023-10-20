# Для какого наименьшего целого неотрицательного числа А выражение
# (5x – 6y < A) ∨ (x – y > 30)
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?

def f(x, y, A):
    return (5 * x - 6 * y < A) or (x - y > 30)

for A in range(1000):
    for x in range(1000):
        for y in range(1000):
            if f(x, y, A) == 0:
                break
        else:
            continue
        break
    else:
        print(A)
        break


# Ответ: 151