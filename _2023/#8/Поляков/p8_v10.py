# Ваня составляет 6-буквенные слова из букв В, И, Д, Е, О. Его интересуют коды, в которых есть хотя бы одна
# буква И и хотя бы одна буква Е. Кроме того, все гласные в слове должны стоять в алфавитном порядке. Сколько
# различных подходящих кодов может составить Ваня?
#
# Ответ: 1215

alf = 'ВИДЕО'
glas = 'ЕИО'
count = 0

for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    for a6 in alf:
                        word = [a1, a2, a3, a4, a5, a6]

                        if 'Е' in word and 'И' in word:
                            kword = [ord(x) for x in word if x in glas]

                            for i in range(len(kword) - 1):
                                if kword[i] > kword[i + 1]:  # важно > т.к. буквы могут повторятся
                                    break
                            else:
                                count += 1


print(count)

