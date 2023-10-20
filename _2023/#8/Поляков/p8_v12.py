# Оля составляет слова перестановкой букв слова СПОРТЛОТО, оставляя только слова с двумя буквами Т рядом.
# Сколько различных слов может составить Оля?
#
# Ответ: 6720

import itertools as it

word = 'СПОРТЛОТО'
permutations = list(it.permutations(word))
# Оборачиваем в множество чтобы исключить повторения, вызванные перестановкой букв О и Т
words = set(["".join(x) for x in permutations])
count = 0

for w in words:
    if 'ТТ' in w:
        count += 1

print(count)


# alf = 'СПОРТЛ'
# count = 0
#
# for a1 in alf:
#     for a2 in alf:
#         for a3 in alf:
#             for a4 in alf:
#                 for a5 in alf:
#                     for a6 in alf:
#                         for a7 in alf:
#                             for a8 in alf:
#                                 for a9 in alf:
#                                     word = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
#
#                                     if word.count('С') == 1 and word.count('П') == 1 and word.count('О') == 3 and\
#                                        word.count('Р') == 1 and word.count('Т') == 2 and word.count('Л') == 1 and\
#                                        'ТТ' in word:
#                                         count += 1
#
# print(count)
