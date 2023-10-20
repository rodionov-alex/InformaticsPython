

def f():
    alf = 'ЛНРТ'
    n = 0

    for a1 in alf:
        for a2 in alf:
            for a3 in alf:
                for a4 in alf:
                    for a5 in alf:
                        n += 1

                        if n == 150:
                            print(a1, a2, a3, a4, a5, sep='')

f()
