from itertools import product

count = 0

for p in product('AAAABBBBB', repeat=6):
    word = ''.join(p)

    if (not (word.startswith('A') or word.endswith('A'))) and 'BAB' not in word:
        count += 1

print(count)
