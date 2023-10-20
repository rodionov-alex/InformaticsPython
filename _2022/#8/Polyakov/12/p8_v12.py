alf = ['З', 'Е', 'Р', 'К', 'А', 'Л', 'О']
count = 0

for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    for a6 in alf:
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if word.count('З') <= 1 and word.count('Е') <= 1 and word.count('Р') <= 1 and\
                           1 <= word.count('К') <= 4 and word.count('А') <= 1 and word.count('Л') <= 1 and\
                           word.count('О') <= 1:
                            count += 1

print(count)
