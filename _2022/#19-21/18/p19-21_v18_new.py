# +100, *2
# win >= 1000
# 1 <= s <= 999

from functools import lru_cache

def moves(a):
    return a + 100, a * 2

@lru_cache(None)
def game(h):
    if h >= 1000:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    # if any(game(m) == 'P1' for m in moves(h)):
    #    return 'V2'
    if all(game(m) == 'P2' for m in moves(h)):
        return 'V2g'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'


results = {}

for s in range(1, 1000):
    r = game(s)

    if r is not None:
        if r in results:
            results[r].append(s)
        else:
            results[r] = [s]

print('P1', results['P1'])
print('V1', results['V1'])
print('P2', results['P2'])
print('V2g', results['V2g'])
print('V2', results['V2'])
print('==================================')
print(len(results['V1']))
print(len(results['P2']))
print(min(results['V2']), max(results['V2']))