# Лёня составляет 5-буквенные слова из букв Э, Ф, Ф, Е, К, Т. Его интересуют коды, в которых все буквы
# различны, при этом все гласные буквы стоят в алфавитном порядке, а все согласные буквы – в обратном
# алфавитном порядке. Сколько различных слов может составить Лёня?
#
# Ответ: 10

alf = 'ЭФЕКТ'
glas = 'ЕЭ'
sogl = 'КТФ'
count = 0

for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    word = [a1, a2, a3, a4, a5]
                    w_glas = [ord(x) for x in word if x in glas]
                    w_sogl = [ord(x) for x in word if x in sogl]
                    lw_glas = len(w_glas)
                    lw_sogl = len(w_sogl)
                    isGood = True

                    if lw_glas > 1:
                        for i in range(lw_glas - 1):
                            if w_glas[i] >= w_glas[i + 1]:  # важно >= т.к. буквы не должны повторятся
                                isGood = False
                                break

                    if isGood and lw_sogl > 1:
                        for i in range(lw_sogl - 1):
                            if w_sogl[i] <= w_sogl[i + 1]:  # важно <= т.к. буквы не должны повторятся
                                isGood = False
                                break

                    if isGood:
                        count += 1

print(count)


