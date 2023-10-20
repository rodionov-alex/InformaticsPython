# +1, *2
# win >= 247
# 17, s
# 1 <= s <= 229

from functools import lru_cache

def moves(w):
    a, b = w
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(h):
    if sum(h) >= 247:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'

for s in range(1, 230):
    res = game((17, s))
    if res is not None:
        print(s, res)

# 58 => min P1 / 2 = 58 с округлением в большую сторону
# 106, 114 => P2
# 105 => min V2