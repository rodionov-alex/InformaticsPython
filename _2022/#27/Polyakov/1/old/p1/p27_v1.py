from tqdm import tqdm
import itertools


def is_good(numb):
    return ((numb % 5 == 0) and (numb % 7 != 0)) or ((numb % 5 != 0) and (numb % 7 == 0))


def combinator(main_list: list, combination: list, cur_index: int, max_sum: int):
    for m in range(len(main_list[cur_index])):
        # Добавление значения в комбинацию
        if cur_index >= len(combination):
            combination.append(main_list[cur_index][m])
        else:
            combination[cur_index] = main_list[cur_index][m]

        if cur_index == len(main_list) - 1:
            r = sum(combination)

            if is_good(max_sum - r):
                return r
        else:
            r = combinator(main_list, combination, cur_index + 1, max_sum)

            if r != 0:
                return r

    return 0


def gcd(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


f = open('27_1a.txt')
lines = f.readlines()[1:]   # Все строки кроме первой
f.close()

lcms = []   # Список списков значений НОК
rasns = []  # Список списков значений разностей
max_rasn_len = 0

for line in lines:
    nums = [int(i) for i in line.split(' ')[1:]]    # Группа чисел (все числа строки кроме первого)
    nums_count = len(nums)                          # Количество чисел
    lcm_group = []                                  # Группа НОК

    for i in range(nums_count - 1):
        for j in range(i + 1, nums_count):
            nok = lcm(nums[i], nums[j])
            # Добавлять в список только уникальные значения НОК
            if nok not in lcm_group:
                lcm_group.append(nok)

    # Сортировка по убыванию, чтобы разности были отсортированы по возрастанию
    lcm_group.sort(reverse=True)
    group_len = len(lcm_group)
    # Только для групп где больше одного значения НОК
    if group_len > 1:
        rasn_list = []          # Список разностей
        max_el = lcm_group[0]   # Максимальный элемент группы
        # Заполнение списка разностей
        for i in range(group_len):
            rasn_list.append(max_el - lcm_group[i])
        # Добавление списка разностей
        rasns.append(rasn_list)
        max_rasn_len = max(max_rasn_len, len(rasn_list))
    # Добавление группы НОК
    lcms.append(lcm_group)

max_sum_lcms = 0
for i in lcms:
    max_sum_lcms += max(i)

comb = []

good_rasn = combinator(rasns, comb, 0, max_sum_lcms)
result = max_sum_lcms - good_rasn

if result != 0:
    print(result)
else:
    print('Fail')


#var = list(itertools.product(*rasns))

#pools = [tuple(pool) for pool in rasns]
#var = [[]]
#for pool in pools:
#    var = [x+[y] for x in var for y in pool]

#for r in var:
#    all_rasns.append(sum(r))
