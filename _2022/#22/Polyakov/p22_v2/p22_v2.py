# Ниже записана программа. Получив на вход число X, эта программа печатает два числа L и M. При каком наибольшем
# значении X после выполнения программы на экран будет выведено сначала число 3, а затем – 7. (Ответ: 65535)

# x = int(input())
# L, M = 0, 0
# while x > 12:
#     L = L + 1
#     x = x // 4
#     M = x
# if L > M:
#     L, M = M, L
# print(L)
# print(M)

# Чтобы найти найти наибольшее X, нужно проанализировать алгоритм и понять, что чем больше X, тем большее
# количество раз выполнится цикл алгоритма. Так же можно заметить что каждую итерацию L увеличивается на 1,
# а значит что для того чтобы вывести результат 3 и 7, цикл должен выполниться либо 3 раза (в случае если L и M
# yне меняются значениями в конце алгоритма) либо 7 раз (для случая когда L будет больше M и они поменяются
# значениями в конце алгоритма). Так как нам важно чтобы цикл выполнялся большее количество раз, то берем
# за основу второй вариант, когда L будет равна 7 и поменяется значением с M. Так же в этм случае очевидно,
# что M в итоге должна принять значение 3, и чтобы этого добиться, нужно определять максимальное число, которое
# при делении на 4 будет давать 3. Для этого строим обратный алгоритм от исходного, т.е. имитирующий работу
# исходного алгоритма задом - на перед.

# Меняем местами значения L и M (обратное от L, M = M, L)
M = 3
L = 7

# Цикл должен выполняться пока L не уменьшится до 0
while L >= 0:
    # Далее идут операторы которые выполняют обратное действие от исходного алгоритма и в обратном порядке:
    x = M                # Обратный оператор от: M = x
    M = (M + 1) * 4 - 1  # Обратный оператор от: x = x // 4
    L -= 1               # Обратный оператор от: L = L + 1

# Вывод получившегося X
print(x)

# P.S. касательно обратного оператора M = (M + 1) * 4 - 1. Здесь, чотбы найти максимальное число которое при делении
# на 4 даст нужный остаток, нужно число увеличить на 1, умножить на 4, и затем вычесть 1. Например, чтобы получить в
# остатке 3 при делении на 4: 3 + 1 это 4; 4 * 4 равно 16; 16 - 1 это 5; 5 же при делении на 4 даст остаток 3, что
# нам и надо.
