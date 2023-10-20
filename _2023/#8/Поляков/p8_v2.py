# Ася составляет семибуквенные слова из букв слова САМОКАТ, причем известно, что буквы в словах могут
# повторяться любое количество раз или же не встречаться вовсе. Помогите Асе найти количество слов, в
# котором один раз встречается комбинация САМ, справа и слева от которой находятся одинаковые гласные буквы.
#
# Ответ: 216

alf = 'САМОКТ'
glas = 'АО'
substr = 'САМ'
w_len = 7


def word_comber(comb, count):
    word = comb

    if len(word) < w_len:
        for a in alf:
            count = word_comber(word + a, count)
    else:
        ind = -1

        if substr in word:
            ind = word.index(substr)

        if 0 < ind < 4:
            al = word[ind - 1]
            ar = word[ind + 3]

            if al == ar and al in glas and ar in glas:
                count += 1

    return count


print(word_comber('', 0))


# alf = 'САМОКТ'
# glas = 'АО'
# substr = 'САМ'
# count = 0
#
# for a1 in alf:
#     for a2 in alf:
#         for a3 in alf:
#             for a4 in alf:
#                 for a5 in alf:
#                     for a6 in alf:
#                         for a7 in alf:
#                             word = a1 + a2 + a3 + a4 + a5 + a6 + a7
#                             ind = -1
#
#                             if substr in word:
#                                 ind = word.index(substr)
#
#                             if 0 < ind < 4:
#                                 al = word[ind - 1]
#                                 ar = word[ind + 3]
#
#                                 if al == ar and al in glas and ar in glas:
#                                     count += 1
#
# print(count)
