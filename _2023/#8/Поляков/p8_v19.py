# Определите количество пятизначных чисел, записанных в девятеричной системе счисления, которые не начинаются
# с нечётных цифр, не оканчиваются цифрами 1 или 8, а также содержат в своей записи не более одной цифры 3.
#
# Ответ: 18944

alf = '012345678'
bad_head = '1357'
bad_tail = '18'
count = 0

for a1 in alf[1:]:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    numb = [a1, a2, a3, a4, a5]

                    if numb[0] not in bad_head and\
                       numb[-1] not in bad_tail and\
                       numb.count('3') <= 1:
                        count += 1

print(count)
