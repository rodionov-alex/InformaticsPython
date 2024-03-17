"""
В файле 17-385.txt содержится последовательность целых неотрицательных чисел, не превышающих 10000.
Определите количество пар элементов последовательности, в которых каждое число больше максимального
из тех элементов последовательности, сумма цифр которых минимальна. В ответе запишите два числа:
сначала количество найденных пар, затем максимальную сумму цифр элементов таких пар. В данной задаче
под парой подразумевается два идущих подряд элемента последовательности.

Ответ: 831 61
"""

def dig_sum(s: str):
    return sum(tuple(map(int, s)))

with open('Data/17-385.txt') as f:
    data = tuple(map(int, f))
    sums = dict()

    for d in data:
        sm = dig_sum(str(d))

        if sm in sums.keys():
            sums[sm].append(d)
        else:
            sums[sm] = [d]

    x = max(sums[min(sums.keys())])
    res = []

    for i in range(1, len(data)):
        if data[i] > x and data[i - 1] > x:
            res.append(dig_sum(str(data[i]) + str(data[i - 1])))

    print(len(res), max(res))
