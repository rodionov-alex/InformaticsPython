from itertools import product

alf = 'РУСЛАН'
p = list(product(alf, repeat=5))
count = 0

for x in p:
    if x.count_t('У') <= 1 and x.count_t('А') <= 1:
        count += 1

print(count)
