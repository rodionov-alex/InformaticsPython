# Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по
# очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один или четыре камня либо
# увеличить количество камней в куче в три раза. У каждого игрока есть неограниченное количество камней,
# чтобы делать ходы.
# Игра завершается в тот момент, когда количество камней в куче становится не менее 55.
# Победителем считается игрок, сделавший последний ход, т.е. первым получивший кучу из 55 камней или
# больше.
# В начальный момент в куче было S камней; 1 ≤ S ≤ 54.
# Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах
# противника.
#
# 19) Укажите минимальное значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети
# Ваня может выиграть своим первым ходом.
# 20) Найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, причём одновременно
# выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
# Найденные значения запишите в ответе в порядке возрастания.
# 21) Найдите минимальное значение S, при котором одновременно выполняются два условия:
# – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
# – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
#
# Ответ: 19) 18
#        20) 6 14
#        21) 13

def f(n, p, m):
    if n >= 55:
        return p % 2 == m % 2
    if p > m:
        return 0
    h = [f(n + 1, p + 1, m), f(n + 4, p + 1, m), f(n * 3, p + 1, m)]
    return any(h) if (p + 1) % 2 == m % 2 else all(h)

for s in range(1, 55):
    for m in range(1, 5):
        if f(s, 0, m):
            print(s, m)