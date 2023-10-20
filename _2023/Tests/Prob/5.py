# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если число N делится на 3, то к этой записи дописываются три последние двоичные цифры;
# б) если число N на 3 не делится, то остаток от деления умножается на 3, переводится в двоичную запись и
# дописывается в конец числа.
# Полученная таким образом запись является двоичной записью искомого числа R.
# 3. Результат переводится в десятичную систему и выводится на экран.
# Например, для исходного числа 12 = 11002 результатом является число 11001002 = 100, а для исходного числа
# 4 = 1002 результатом является число 100112 = 19.
# Укажите максимальное число N, после обработки которого с помощью этого алгоритма получается число R,
# меньшее чем 76
#
# Ответ: 16

for n in range(4, 10000):
    bn = bin(n)[2:]

    if n % 3 == 0:
        bn += bn[-3:]
    else:
        bn += bin(n % 3 * 3)[2:]

    r = int(bn, 2)

    if r < 76:
        print(n)