# +1, *2
# 50 <= win <= 70
# 1 <= s <= 49

from functools import lru_cache

def moves(a):
    return a + 1, a * 2

@lru_cache(None)
def game(h):
    if 50 <= h <= 70:
        return 'W'
    if h > 70:
        return 'P1'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'

for s in range(1, 50):
    res = game(s)
    if res is not None:
        print(s, res)

# 13        (P1 25 / 2 ~~ 13)
# 24, 47    (P2)
# 46        (V2)