# Оля составляет слова перестановкой букв слова СПОРТЛОТО, оставляя только слова с тремя буквами О рядом.
# Сколько различных слов может составить Оля?
#
# Ответ: 2520

import itertools as it

word = 'СПОРТЛОТО'
permutations = list(it.permutations(word))
# Оборачиваем в множество чтобы исключить повторения, вызванные перестановкой букв О и Т
words = set(["".join(x) for x in permutations])
count = 0

for w in words:
    if 'ООО' in w:
        count += 1

print(count)
