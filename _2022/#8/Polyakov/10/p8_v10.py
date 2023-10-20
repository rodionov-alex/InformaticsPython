alf = 'КУСАТЬ'
count = 0

for a1 in alf:
    if a1 == 'Ь':
        continue

    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('К') <= 1 and word.count('У') <= 1 and word.count('С') <= 1 and\
                       word.count('А') <= 1 and word.count('Т') <= 1 and word.count('Ь') <= 1 and\
                       "СУК" not in word:
                        count += 1

print(count)
