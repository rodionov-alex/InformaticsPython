def find_word_ind(word):
    abc1 = ['В', 'К', 'Н', 'С', 'Т']
    abc2 = ['А', 'В', 'И', 'К', 'Н', 'С', 'Т']
    abc3 = ['А', 'И']

    ind = 0

    for p1 in abc1:
        for p2_1 in abc2:
            for p2_2 in abc2:
                for p3 in abc3:
                    ind += 1

                    if p1 + p2_1 + p2_2 + p3 == word:
                        return ind


print(find_word_ind('НИКА'))
