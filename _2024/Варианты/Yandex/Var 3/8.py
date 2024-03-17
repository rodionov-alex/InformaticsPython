from itertools import permutations

print(len([x for x in permutations('кабинет') if x[-1] not in 'аие']))
