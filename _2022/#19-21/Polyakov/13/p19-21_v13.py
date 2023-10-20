# +1, +2, +3, *2
# win > 33
# 1 <= s <= 33

from functools import lru_cache

def moves(a):
    return a + 1, a + 2, a + 3, a * 2

@lru_cache(None)
def game(h):
    if h > 33:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'

for s in range(1, 34):
    res = game(s)
    if res is not None:
        print(s, res)

# 16    (V1)
# 8, 15 (min max P2)
# 12    (V2)