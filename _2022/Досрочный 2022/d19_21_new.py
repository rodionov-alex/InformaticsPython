# +1, *2
# >= 223
# 17; s
# 1 <= s <= 205

from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(h):
    if sum(h) >= 223:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'

for s in range(1, 206):
    res = game( (17, s) )
    if res is not None:
        print(s, res)

# 52 (минимальное P1 = 103; 103 / 2 ~~ 52 так как действие с наибольшим результатом это *2)
# 94, 102 (94 P2, 102 P2)
# 93 (минимальное V2 = 93)