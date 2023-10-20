s = '0122233'
print(s)

while ('01' in s) or ('02' in s) or ('03' in s):
    s = s.replace('01', '302', 1)
    s = s.replace('02', '3103', 1)
    s = s.replace('03', '20', 1)

print(s)
print('1: ', s.count('1'))
print('2: ', s.count('2'))
print('3: ', s.count('3'))

# Выполнив данный алгоритм  с разным количеством единиц, двоек и троек можно заметить следующую закономерность:
# - во время работы алгоритма ноль постепенно передвигается в конец строки;
# - конечное количество цифр зависит от их количества в исходной троке;
#
# Количество 1 зависит от количества '1' и '2' в исходной строке
# Количество 2 зависит от количества '1', '2' и '3' в исходной строке
# Количество 3 зависит от количества '1' и '3' в исходной строке
#
# Если в итоге получили 18 единиц, 39 двоек и 25 троек, тогда исходная строка состояла из 39 символов и в ней было
# 18 единиц или двоек, и 25 единиц или троек.
# Итого 18 + 25 = 43 символа единиц или двоек и единиц или троек, но по второй закономерности было всего 39 символов...
# Так как единицы есть в обоих случаях, то их количество равно 43 - 39 = 4 единцы, а значит троек было 25 - 4 = 21.
# Ответ: 21
