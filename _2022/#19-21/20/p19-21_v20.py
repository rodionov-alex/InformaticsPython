# (a,b)=>(a+b,b)
# win >= 45

from functools import lru_cache

def moves(w):
    a, b = w
    return (a + b, b), (a, a + b)

@lru_cache(None)
def game(h):
    if sum(h) >= 45:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'

pos = 7
print('------- (7, s) --------')

for s in range(1, 45 - pos):
    res = game((pos, s))
    if res is not None:
        print(s, res)

pos = 6
print('------- (6, s) --------')

for s in range(1, 45 - pos):
    res = game((pos, s))
    if res is not None:
        print(s, res)

pos = 0
print('------- (s, s) --------')

for s in range(1, 45 - pos):
    res = game((s, s))
    if res is not None:
        print(s, res)
