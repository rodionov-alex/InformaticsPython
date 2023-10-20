# Алексей составляет пятибуквенные слова из букв латинского алфавита. Его интересуют слова, в которых не менее
# одной гласной. Сколько таких слов может составить Алексей?
#
# Ответ: 8681376

from string import ascii_uppercase

glas = 'AEIOUY'
count = 0

for a1 in ascii_uppercase:
    for a2 in ascii_uppercase:
        for a3 in ascii_uppercase:
            for a4 in ascii_uppercase:
                for a5 in ascii_uppercase:
                    if a1 in glas or a2 in glas or a3 in glas or a4 in glas or a5 in glas:
                        count += 1

print(count)
