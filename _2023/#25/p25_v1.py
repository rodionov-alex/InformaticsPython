# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и
# пустую последовательность.
# Среди натуральных чисел, не превышающих 17 * 10^6, найдите все числа, соответствующие маске *1?*?68*, делящиеся
# на 161 без остатка. В ответе запишите в первом столбце таблицы каждое пятисотое найденное число, начиная с первого,
# в порядке возрастания (1-е, 501-е, 1001-е....), а во втором столбце – соответствующие им результаты деления этих
# чисел на 161.
#
# Ответ: 14168 88
#        10658683 66203
#        12668285 78685
#        14702681 91321
#        16738687 103967

# region Old
import itertools

res = set()
max_comb_len = 3
digits = '0123456789'

# *1?*?68*
# x1ayb68z

allcombs = []

for i in range(max_comb_len + 1):
    combs = set()
    for j in itertools.product(digits, repeat=i):
        combs.add(''.join(j))
    allcombs.append(sorted(combs))

for a in digits:
    for b in digits:
        for xi in range(max_comb_len + 1):
            for x in allcombs[xi]:
                max_y = max_comb_len - xi

                for yi in range(max_y + 1):
                    for y in allcombs[yi]:
                        max_z = max_comb_len - xi - yi

                        for zi in range(max_z + 1):
                            for z in allcombs[zi]:
                                num = int(x + '1' + a + y + b + '68' + z)

                                if num <= 17 * 10 ** 6 and num % 161 == 0:
                                    res.add(num)

res = sorted(res)

for i in range(0, len(res), 500):
    print(res[i], res[i] // 161)
# endregion

# region Regular Expressions
import re

res = []

for n in range(161, 17 * 10 ** 6 + 1, 161):
    if re.fullmatch(r'\d*1\d\d*\d68\d*', str(n)) is not None:
        res.append(n)

print(len(res))


for i in range(0, len(res), 500):
    print(res[i], res[i] // 161)
# endregion
