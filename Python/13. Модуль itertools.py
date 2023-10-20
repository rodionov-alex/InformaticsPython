# Подключаемый модуль itertools содержит массу полезных фукнций-итераторов.

import itertools

# product - аналог вложенных циклов, возвращает все возможные комбинации элементов заданной длины.
print('product')
print(list(itertools.product('ABC', repeat=2)))
print(list(itertools.product((0, 1), repeat=3)))
print()

# permutations - возвращает все возможные перестановки.
print('permutations')
print(list(itertools.permutations('ABC')))
print(list(itertools.permutations('ABC', r=2)))
print()

# itertools.combinations(iterable, [r]) - возвращает комбинации длиной r из iterable без повторяющихся элементов,
#                                         сохраняя их порядок.
print('combinations')
print(list(itertools.combinations('ABC', r=2)))
print()

# itertools.combinations_with_replacement(iterable, r) - возвращает комбинации длиной r из iterable с
#                                                        повторяющимися элементами.
print('combinations_with_replacement')
print(list(itertools.combinations_with_replacement('ABC', r=2)))
print()

# itertools.repeat(elem, n=Inf) - повторяет elem n раз.
print('repeat')
print(list(itertools.repeat(1, 5)))
print()

# itertools.accumulate(iterable) - аккумулирует суммы.
print('accumulate')
print(list(itertools.accumulate((0, 1, 2, 3, 4, 5))))
print()

# itertools.chain(*iterables) - возвращает по одному элементу из первого итератора, потом из второго, до тех пор,
#                               пока итераторы не кончатся.
print('chain')
print(list(itertools.chain('ABC', 'DEF')))
print()
