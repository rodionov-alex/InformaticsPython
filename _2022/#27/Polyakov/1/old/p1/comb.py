from tqdm import tqdm


def combinator_p(main_list: list, combination: list, cur_index: int, result: list):
    for m in tqdm(range(len(main_list[cur_index]))):
        # Добавление значения в комбинацию
        if cur_index >= len(combination):
            combination.append(main_list[cur_index][m])
        else:
            combination[cur_index] = main_list[cur_index][m]

        if cur_index == len(main_list) - 1:
            result.append(combination[:])
        else:
            combinator(main_list, combination, cur_index + 1, result)


def combinator(main_list: list, combination: list, cur_index: int, result: list):
    for m in range(len(main_list[cur_index])):
        # Добавление значения в комбинацию
        if cur_index >= len(combination):
            combination.append(main_list[cur_index][m])
        else:
            combination[cur_index] = main_list[cur_index][m]

        if cur_index == len(main_list) - 1:
            result.append(combination[:])
        else:
            combinator(main_list, combination, cur_index + 1, result)


list_of_lists = []
results = []
tmp = []

#region Initialize
# 0
for i in range(6):
    tmp.append(i)

list_of_lists.append(tmp[:])
tmp.clear()

# 1
for i in range(5):
    tmp.append(i)

list_of_lists.append(tmp[:])
tmp.clear()

#2
for i in range(7):
    tmp.append(i)

list_of_lists.append(tmp[:])
tmp.clear()

# 3
for i in range(2):
    tmp.append(i)

list_of_lists.append(tmp[:])
tmp.clear()

# 4
for i in range(4):
    tmp.append(i)

list_of_lists.append(tmp[:])
tmp.clear()

# 5
for i in range(3):
    tmp.append(i)

list_of_lists.append(tmp[:])
tmp.clear()
#endregion

re = []
cb = []

combinator_p(list_of_lists, cb, 0, re)
print(re)
max_len = 0

for v in list_of_lists:
    max_len = max(max_len, len(v))

# Print
for i in range(max_len):
    for v in list_of_lists:
        if i < len(v):
            tmp.append(v[i])
        else:
            tmp.append(0)

    print(tmp)
    tmp.clear()

#for l in range(len(list_of_lists) - 1):
#    for i in range(len(list_of_lists[l])):
#        for p in range(l + 1, len(list_of_lists)):
#            for j in range(len(list_of_lists[p])):


