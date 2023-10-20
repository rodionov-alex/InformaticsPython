from itertools import permutations

forbidden = ['НД', 'ДН', 'ОА', 'АО']
words = [''.join(x) for x in permutations('НОДА', r=4)]
print(len(set(x for x in words if all(y not in x for y in forbidden))))
