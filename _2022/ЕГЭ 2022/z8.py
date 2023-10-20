def find_word():
    alf = 'АЛПЦЯ'
    i = 0

    for a1 in alf:
        for a2 in alf:
            for a3 in alf:
                for a4 in alf:
                    for a5 in alf:
                        i += 1
                        word = a1 + a2 + a3 + a4 + a5

                        if word.count('А') <= 1 and word.count('Ц') == 2 and 'Л' not in word:
                            return i, word

print(find_word())