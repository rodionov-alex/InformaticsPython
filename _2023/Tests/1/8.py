alf = 'POLYGN'
gl = 'OY'
count = 0
words = set()

for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    word = a1 + a2 + a3 + a4 + a5

                    if a3 in gl and word == word[::-1]:
                        words.add(word)

print(len(words))