from math import factorial
from functools import lru_cache

with open('27-59a.txt') as f:
    nums = list(map(int, f.readlines()[1:]))

    mods = [0] * 10

    for n in nums:
        mods[n % 10] += 1

    ind = [x for x in range(10)]
    print(ind)
    print(mods)

@lru_cache(None)
def fact(x):
    return factorial(x)

# 0 + 5
# 1 + 4
# 2 + 3
# 6 + 9
# 7 + 8


#def f(index, sm, md, res):
