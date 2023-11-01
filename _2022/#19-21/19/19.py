# +3, +13, +23
# win >= 73
# 2, s, 2s
# 1 <= s <= 23

from tqdm import tqdm
from functools import lru_cache

def moves(w):
   a, b, c = w
   return (a + 3, b, c), (a, b + 3, c), (a, b, c + 3),\
          (a + 13, b, c), (a, b + 13, c), (a, b, c + 13),\
          (a + 23, b, c), (a, b + 23, c), (a, b, c + 23)

#@lru_cache(None)
def game(h):
    if sum(h) >= 73:
        return 'Win'
    if any(game(m) == 'Win' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P2' for m in moves(h)):
        return 'V2 only'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V12'


for s in tqdm(range(1, 24)):
    res = game((2, s, 2 * s))

    if res is not None:
        print(s, res)