def f():
    alf = ['А', 'П', 'Р', 'С', 'У']
    i = 0

    for a1 in alf:
        for a2 in alf:
            for a3 in alf:
                for a4 in alf:
                    for a5 in alf:
                        word = a1 + a2 + a3 + a4 + a5
                        i += 1

                        if a1 == 'У' and 'АА' not in word:
                            return i

print(f())

