# Миша составляет все возможные пятибуквенные слова из букв латинского алфавита. Найдите общее число гласных
# во всех этих словах.
#
# Ответ: 13709280

from string import ascii_uppercase
from itertools import product

glas = 'AEIOUY'
count = 0
ln = 5

for word in product(ascii_uppercase, repeat=ln):
    for i in range(ln):
        if word[i] in glas:
            count += 1

print(count)
