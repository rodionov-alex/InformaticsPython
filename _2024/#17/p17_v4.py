"""
В файле 17-382.txt содержится последовательность натуральных чисел. Элементы последовательности могут
принимать целые значения от 1 до 10 000 включительно. Определите количество пар последовательности, в
которых только одно число имеет отличное от 3 количество разрядов, а элементы пары отличаются на значение,
кратное минимальному трехзначному значению в последовательности, оканчивающемуся на 11. В ответе запишите
количество найденных пар, затем максимальную из сумм элементов таких пар. В данной задаче под парой
подразумевается два идущих подряд элемента последовательности.

Ответ:
"""
def is_3(n):
    return 100 <= n <= 999


with (open('Data/17-382.txt') as f):
    data = tuple(map(int, f))
    mn = min([x for x in data if is_3(x) and x % 100 == 11])
    res = []

    for i in range(1, len(data)):
        if is_3(data[i]) and (not is_3(data[i - 1])) or is_3(data[i - 1]) and (not is_3(data[i])):
            if abs(data[i] - data[i - 1]) % mn == 0:
                res.append(data[i] + data[i - 1])

    print(len(res), max(res))