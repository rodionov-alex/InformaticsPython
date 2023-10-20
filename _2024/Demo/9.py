# Откройте файл электронной таблицы, содержащей в каждой строке семь
# натуральных чисел. Определите количество строк таблицы, для чисел
# которых выполнены оба условия:
# – в строке есть два числа, каждое из которых повторяется дважды,
# остальные три числа различны;
# – среднее арифметическое всех повторяющихся чисел строки меньше
# среднего арифметического всех её чисел.
# В ответе запишите только число.

def avg(lst):
    return sum(lst) / len(lst)


with open('9.txt') as f:
    data = [list(map(int, x.split())) for x in f.readlines()]
    count = 0

    for d in data:
        davg = avg(d)
        povt = []

        for n in d:
            if d.count(n) == 2:
                povt.append(d.pop(d.index(n)))
                povt.append(d.pop(d.index(n)))

        if len(povt) == 4 and avg(povt) < davg:
            count += 1

    print(count)

# Ответ: 83
