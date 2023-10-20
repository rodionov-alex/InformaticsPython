alf = 'БРОНХИ'
count = 0

for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                word = [a1, a2, a3, a4]

                if word.count('Х') == 1:
                    count += 1

print(count)
