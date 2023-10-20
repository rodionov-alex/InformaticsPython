 # Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m»;
# и пусть на числовой прямой дан отрезок B = [10; 40]. Найдите наименьшую возможную длину отрезка A, при
# котором формула
# (x ∈ A) ∨ ((x ∈ B) → ¬ДЕЛ(x, 6))
# тождественно истинна, то есть принимает значение 1 при любом натуральном значении переменной х?
#
# Ответ: 24

def d(n, m):
    return n % m == 0


A = set()
b1, b2 = 10, 40
B = [i for i in range(b1, b2 + 1)]


def f(x):
    return (x in A) or ((x in B) <= (not d(x, 6)))


for x in B:
    if not f(x):
        A.add(x)

print(max(A) - min(A))
