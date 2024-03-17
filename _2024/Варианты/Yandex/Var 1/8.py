from itertools import product

words = [''.join(x) for x in product('АЕКПТЧ', repeat=7)]
print(words.index('ПЕЧАТКА') - words.index('АПТЕЧКА') - 1)

