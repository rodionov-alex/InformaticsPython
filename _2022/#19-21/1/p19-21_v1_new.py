# /2 if %2 or -2
# /3 if %3 or -3
# win = 1
# 1 <= s <= 37

from functools import lru_cache

def f2(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x - 2

def f3(x):
    if x % 3 == 0:
        return x // 3
    else:
        return x - 3

def moves(a):
    return f2(a), f3(a)

@lru_cache(None)
def game(h):
    if h == 1:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'

for s in range(1, 38):
    res = game(s)

    if res is not None:
        print(s, res)

# 4 (min P1 * 2 так как четное и *2 дает наибольший результат)
# 7, 18 (P2)
# 9 (V2)