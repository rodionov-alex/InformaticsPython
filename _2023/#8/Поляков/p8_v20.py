# Определите количество пятизначных чисел, записанных в восьмеричной системе счисления, в записи которых
# ровно одна цифра 6, при этом никакая нечётная цифра не стоит рядом с цифрой 6.
#
# Ответ: 2961

alf = '01234567'
bad = '1357'
count = 0

for a1 in alf[1:]:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    numb = [a1, a2, a3, a4, a5]

                    if numb.count('6') == 1:
                        ind = numb.index('6')

                        if (ind == 0 or numb[ind - 1] not in bad) and \
                           (ind == len(numb) - 1 or numb[ind + 1] not in bad):
                            count += 1

print(count)
