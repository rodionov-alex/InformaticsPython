alf = 'ТИМОФЕЙ'
n = 0

for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    word = [a1, a2, a3, a4, a5]

                    if word.count('Т') >= 1 >= word.count('Й'):
                        n += 1

print(n)