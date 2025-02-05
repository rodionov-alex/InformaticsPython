"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней, в каждой из них не менее
одного камня. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в большую кучу
любое количество камней от одного до трёх или удвоить количество камней в меньшей куче. Если кучи содержат равное
количество камней, можно добавить в любую из них от одного до трёх камней, удвоение в этой ситуации запрещено.
Игра завершается, когда общее количество камней в любой из двух куч становится больше или равно 78. Победителем
считается игрок, сделавший последний ход, то есть первым получивший 78 в одной куче.

Ответьте на следующие вопросы:
    Вопрос 1. Известно, что Петя смог выиграть первым ходом. Какое наименьшее число камней могло быть суммарно в
    двух кучах?

    Вопрос 2. Известно, что в первой куче 25 камней, а во второй – S камней (1 ≤ S ≤ 77). Найдите наименьшее и
    наибольшее значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
        – Петя не может выиграть за один ход;
        – Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
    Запишите в ответе сначала наименьшее значение, потом – наибольшее.

    Вопрос 3. Известно, что в первой куче 69 камней, а во второй – S камней (1 ≤ S ≤ 77). Найдите значение S, при
    котором одновременно выполняются два условия:
        — у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
        — у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

Ответы: 76
        50 73
        35
"""

def minmax(lst):
    return min(lst), max(lst)

def f(s1, s2, m):
    if s1 >= 78 or s2 >= 78:
        return m % 2 == 0

    if m == 0:
        return 0

    h = []

    for i in range(1, 4):
        if s1 == s2:
            h.append(f(s1 + i, s2, m - 1))
            h.append(f(s1, s2 + i, m - 1))
        elif s1 > s2:
            h.append(f(s1 + i, s2, m - 1))
        else:
            h.append(f(s1, s2 + i, m - 1))

        if s1 != s2:
            h.append(f(s1 * 2, s2, m - 1) if s1 < s2 else f(s1, s2 * 2, m - 1))

    return any(h) if (m - 1) % 2 == 0 else all(h)

print('19)', min([s for s in range(1, 77) if f(1, s, 1)]) + 1)
print('20)', *minmax([s for s in range(1, 78) if not f(25, s, 1) and f(25, s, 3)]))
print('21)', *[s for s in range(1, 78) if not f(69, s, 2) and f(69, s, 4)])
