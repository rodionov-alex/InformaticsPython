# +1, *2
# 30 <= win <= 45
# 1 <= s <= 29

from functools import lru_cache

def moves(w):
    return w + 1, w * 2

@lru_cache(None)
def game(h):
    if 30 <= h <= 45:
        return 'W'
    if h > 45:
        return 'P1'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'

for s in range(1, 30):
    res = game(s)
    if res is not None:
        print(s, res)

# 8
# 14 27
# 26