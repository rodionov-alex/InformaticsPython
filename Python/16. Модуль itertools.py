# Подключаемый модуль itertools содержит массу полезных фукнций-итераторов.

import itertools

print('-=-=-= КОМБИНАТОРИКА =-=-=-')

# product(*args, repeat: int) - аналог вложенных циклов, возвращает все возможные комбинации элементов заданной длины.
print('product:')
print('itertools.product(\'ABC\', repeat=2) ->')
print(*(itertools.product('ABC', repeat=2)))
print('itertools.product((0, 1), repeat=3) ->')
print(*(itertools.product((0, 1), repeat=3)))
print()

# permutations(iterable, r: int) - возвращает все возможные перестановки.
print('permutations:')
print('itertools.permutations(\'ABC\') ->')
print(*(itertools.permutations('ABC')))
print('itertools.permutations(\'ABC\', r=2) ->')
print(*(itertools.permutations('ABC', r=2)))
print()

# itertools.combinations(iterable, r) - возвращает комбинации длиной r из iterable без повторяющихся элементов,
#                                         сохраняя их порядок.
print('combinations:')
print('itertools.combinations(\'ABC\', r=2) ->')
print(*(itertools.combinations('ABC', r=2)))
print()

# itertools.combinations_with_replacement(iterable, r) - возвращает комбинации длиной r из iterable с
#                                                        повторяющимися элементами.
print('combinations_with_replacement')
print('itertools.combinations_with_replacement(\'ABC\', r=2) ->')
print(*(itertools.combinations_with_replacement('ABC', r=2)))
print()


print('-=-=-= ОСТАЛЬНЫЕ ФУНКЦИИ =-=-=-')

# itertools.accumulate(iterable) - аккумулирует суммы: p0, p0+p1, p0+p1+p2, ...
print('accumulate:')
print('itertools.accumulate([0, 1, 2, 3, 4, 5]) ->')
print(*(itertools.accumulate([0, 1, 2, 3, 4, 5])))
print()

# itertools.chain(*iterables) - возвращает по одному элементу из первого итератора, потом из второго, до тех пор,
#                               пока итераторы не кончатся.
print('chain:')
print('itertools.chain(\'CBA\', \'DEF\') ->')
print(*(itertools.chain('CBA', 'DEF')))
print()

# itertools.compress(data: iterable, selectors: iterable) - фильтрует итератор data по маске итератора selectors
print('compress:')
print('itertools.compress(\'ABCDEFG\', [1, 1, 0, 0, 1, 0, 1]) ->')
print(*(itertools.compress('ABCDEFG', [1, 1, 0, 0, 1, 0, 1])))
print()

# itertools.repeat(elem, n=Inf) - повторяет elem n раз.
print('repeat:')
print('itertools.repeat(1, 5) ->')
print(*(itertools.repeat(1, 5)))
print()

# itertools.filterfalse(function, iterable) - фильтрует элементы, оставляя те, для которых функция возвращает ложь.
print('filterfalse:')
print('itertools.filterfalse(lambda x: x % 2 == 0, range(10)) ->')
print(*(itertools.filterfalse(lambda x: x % 2 == 0, range(10))))
print()

# itertools.starmap(function, iterable) - применяет функцию к каждому элементу последовательности (каждый элемент
#                                         распаковывается).
print('starmap:')
print('itertools.starmap(pow, [(2,5), (3,2), (10,3)]) ->')
print(*(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])))
print()

# itertools.takewhile(function, iterable) - пока function возвращает true копирует элементы из iterable.
#                                           Возвращает скопированные элементы.
print('takewhile:')
print('itertools.takewhile(lambda x: x < 5, [3, 4, 5, 4, 3]) ->')
print(*(itertools.takewhile(lambda x: x < 5, [3, 4, 5, 4, 3])))
print()

# itertools.dropwhile(function, iterable) - пока function возвращает true пропускает элементы iterable.
#                                           Возвращает копии оставшихся элементов.
print('dropwhile:')
print('itertools.dropwhile(lambda x: x < 5, [3, 4, 5, 4, 3]) ->')
print(*(itertools.dropwhile(lambda x: x < 5, [3, 4, 5, 4, 3])))
print()

# itertools.zip_longest(*iterables, fillvalue=None) - аналог функции zip но берет самый длинный итератор, а более
#                                                     короткие дополняет fillvalue.
print('dropwhile:')
print('itertools.zip_longest(\'ABCD\', \'xy\', fillvalue=\'*\') ->')
print(*(itertools.zip_longest('ABCD', 'xy', fillvalue='*')))
print()
