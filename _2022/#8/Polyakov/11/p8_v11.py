alf = 'ОДЕКЛН'
count = 0

for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    for a6 in alf:
                        for a7 in alf:
                            for a8 in alf:
                                word = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

                                if word.count('О') == 3 and word.count('Д') == 1 and word.count('Е') == 1 and \
                                   word.count('К') == 1 and word.count('Л') == 1 and word.count('Н') == 1 and \
                                   "ОО" not in word:
                                    count += 1

print(count)
