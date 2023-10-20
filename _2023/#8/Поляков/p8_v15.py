# Оля составляет слова перестановкой букв слова СПОРТЛОТО, оставляя только слова с различными буквами в начале
# и в конце. Сколько различных слов может составить Оля?
#
# Ответ: 26880

import itertools as it

word = 'СПОРТЛОТО'
permutations = list(it.permutations(word))
# Оборачиваем в множество чтобы исключить повторения, вызванные перестановкой букв О и Т
words = set(["".join(x) for x in permutations])
count = 0

for w in words:
    if w[0] != w[-1]:
        count += 1

print(count)
